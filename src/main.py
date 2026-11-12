"""
Entry point for the dev-remote-jobs-monitor pipeline.

Runs the crawler, writes data/jobs.json + data/stats.json and refreshes the
auto-generated sections of README.md.

Safety net: if the crawl returns nothing (or loses more than half of the
listings compared to the previous run) the script aborts *without* writing, so
a broken upstream feed can never wipe the public API.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from urllib.parse import quote
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.fetcher import get_all_jobs  # noqa: E402

DATA_DIR = os.path.join(ROOT, "data")
JOBS_PATH = os.path.join(DATA_DIR, "jobs.json")
STATS_PATH = os.path.join(DATA_DIR, "stats.json")
FEED_PATH = os.path.join(DATA_DIR, "feed.xml")
README_PATH = os.path.join(ROOT, "README.md")

MIN_EXPECTED_JOBS = 20
MAX_DROP_RATIO = 0.5
README_TABLE_SIZE = 25
README_BADGE_COUNT = 8

JOBS_START, JOBS_END = "<!-- JOBS_START -->", "<!-- JOBS_END -->"
STATS_START, STATS_END = "<!-- STATS_START -->", "<!-- STATS_END -->"


# --------------------------------------------------------------------------- #
# Stats
# --------------------------------------------------------------------------- #
def build_stats(jobs: list[dict]) -> dict:
    tag_counts = Counter(tag for job in jobs for tag in job.get("tags", []))
    return {
        "last_updated": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "total_jobs": len(jobs),
        "top_tags": dict(tag_counts.most_common(20)),
        "categories": dict(
            Counter(job.get("category", "General") for job in jobs).most_common()
        ),
        "regions": dict(
            Counter(job.get("region", "other") for job in jobs).most_common()
        ),
        "seniority": dict(
            Counter(job.get("seniority") or "unknown" for job in jobs).most_common()
        ),
        "sources": dict(
            Counter(job.get("source", "Unknown") for job in jobs).most_common()
        ),
        "salary_coverage": round(
            sum(1 for job in jobs if job.get("salary")) / len(jobs) * 100
        )
        if jobs
        else 0,
    }


def previous_total() -> int:
    try:
        with open(JOBS_PATH, encoding="utf-8") as handle:
            return len(json.load(handle))
    except (OSError, ValueError, TypeError):
        return 0


# --------------------------------------------------------------------------- #
# README rendering
# --------------------------------------------------------------------------- #
def _cell(value: str) -> str:
    """Make a value safe inside a Markdown table cell."""
    return (value or "").replace("|", "-").replace("\n", " ")


def _display_date(iso: str) -> str:
    """ISO in the data, dd/mm/yyyy in the README (Argentine format)."""
    try:
        return datetime.strptime((iso or "")[:10], "%Y-%m-%d").strftime("%d/%m/%Y")
    except (TypeError, ValueError):
        return iso or ""


def _badge(label: str, count: int) -> str:
    # shields.io: "-" -> "--", "_" -> "__", spaces -> "_" (or %20, both render).
    escaped = label.replace("-", "--").replace("_", "__").replace(" ", "_")
    encoded = quote(escaped, safe="")
    return (
        f"![{label}](https://img.shields.io/badge/{encoded}-{count}%20vacantes-indigo)"
    )


def generate_markdown_table(jobs: list[dict], limit: int = README_TABLE_SIZE) -> str:
    lines = [
        "| Puesto | Empresa | Categoría | Tags | Ubicación | Fecha |",
        "|:-------|:--------|:----------|:-----|:----------|:------|",
    ]
    for job in jobs[:limit]:
        title = _cell(job.get("title", ""))
        company = _cell(job.get("company", ""))
        url = job.get("url") or "#"
        tags = " ".join(f"`{tag}`" for tag in job.get("tags", [])[:3]) or "-"
        location = _cell(job.get("location", "Remote"))
        lines.append(
            f"| **[{title}]({url})** | {company} | `{job.get('category', 'General')}` "
            f"| {tags} | {location} | {_display_date(job.get('date', ''))} |"
        )
    return "\n".join(lines)


def generate_stats_block(stats: dict) -> str:
    badges = " ".join(
        _badge(tag, count)
        for tag, count in list(stats.get("top_tags", {}).items())[:README_BADGE_COUNT]
    )
    coverage = stats.get("salary_coverage", 0)
    sources = len(stats.get("sources", {}))
    return (
        "\n### Tecnologías con más demanda hoy\n\n"
        f"{badges}\n\n"
        f"<sub>{stats['total_jobs']} ofertas activas · "
        f"{sources} fuentes · "
        f"{coverage}% con salario publicado · "
        f"actualizado cada 6 h</sub>\n"
    )


def _replace_block(content: str, start: str, end: str, block: str) -> str:
    if start not in content or end not in content:
        return content
    head, _, rest = content.partition(start)
    _, _, tail = rest.partition(end)
    return f"{head}{start}{block}{end}{tail}"


def update_readme(jobs: list[dict], stats: dict) -> bool:
    if not os.path.exists(README_PATH):
        print("[!] README.md not found, skipping README update")
        return False

    with open(README_PATH, encoding="utf-8") as handle:
        content = handle.read()

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    jobs_block = (
        f"\n*Última actualización automática: **{stamp}** · "
        f"Ofertas activas: **{len(jobs)}***\n\n"
        f"{generate_markdown_table(jobs)}\n\n"
    )

    original = content
    content = _replace_block(content, JOBS_START, JOBS_END, jobs_block)
    content = _replace_block(
        content, STATS_START, STATS_END, generate_stats_block(stats)
    )

    if content == original:
        print("[!] README markers not found, nothing replaced")
        return False

    with open(README_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)
    return True


# --------------------------------------------------------------------------- #
# Persistence
# --------------------------------------------------------------------------- #
def write_json(path: str, payload: object) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


# --------------------------------------------------------------------------- #
# RSS feed (open subscription format, no keys involved)
# --------------------------------------------------------------------------- #
def _rfc822(iso_date: str) -> str:
    """Turn YYYY-MM-DD into the RFC 822 date RSS readers expect."""
    try:
        day = datetime.strptime(iso_date[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        day = datetime.now(timezone.utc).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
    return day.strftime("%a, %d %b %Y %H:%M:%S +0000")


def build_feed(
    jobs: list[dict],
    *,
    limit: int = 100,
    last_build: str | None = None,
) -> str:
    """Build an RSS 2.0 feed so anyone can subscribe without an API key."""
    stamp = last_build or datetime.now(timezone.utc).strftime(
        "%a, %d %b %Y %H:%M:%S +0000"
    )
    items = []
    for job in jobs[:limit]:
        title = escape(
            f"{job.get('title', 'Untitled')} — {job.get('company', '')}".strip(" —")
        )
        details = " · ".join(
            part
            for part in (
                job.get("company", ""),
                job.get("location", ""),
                job.get("category", ""),
                ", ".join(job.get("tags", [])),
                job.get("salary") or "",
                job.get("source", ""),
            )
            if part
        )
        items.append(
            "    <item>\n"
            f"      <title>{title}</title>\n"
            f"      <link>{escape(job.get('url', ''))}</link>\n"
            f'      <guid isPermaLink="false">{escape(job.get("id", ""))}</guid>\n'
            f"      <pubDate>{_rfc822(job.get('date', ''))}</pubDate>\n"
            f"      <category>{escape(job.get('category', 'General'))}</category>\n"
            f"      <description>{escape(details)}</description>\n"
            "    </item>"
        )

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        "  <channel>\n"
        "    <title>DevJobs Remote — vacantes remotas para desarrolladores</title>\n"
        "    <link>https://leandrocarlino.github.io/dev-remote-jobs-monitor/</link>\n"
        "    <description>Ofertas remotas de desarrollo, actualizadas cada 6 horas. "
        "Incluye vacantes de Latam y Argentina.</description>\n"
        "    <language>es-AR</language>\n"
        f"    <lastBuildDate>{stamp}</lastBuildDate>\n"
        '    <atom:link href="https://leandrocarlino.github.io/dev-remote-jobs-monitor/feed.xml" '
        'rel="self" type="application/rss+xml"/>\n'
        f"{chr(10).join(items)}\n"
        "  </channel>\n"
        "</rss>\n"
    )


def write_feed(jobs: list[dict]) -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(FEED_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(build_feed(jobs))


def guard(jobs: list[dict], force: bool) -> str | None:
    """Return an error message when the result looks like a failed crawl."""
    if force:
        return None
    if len(jobs) < MIN_EXPECTED_JOBS:
        return f"only {len(jobs)} listings (minimum {MIN_EXPECTED_JOBS})"
    previous = previous_total()
    if previous >= MIN_EXPECTED_JOBS and len(jobs) < previous * MAX_DROP_RATIO:
        return f"listing count fell from {previous} to {len(jobs)} (>{MAX_DROP_RATIO:.0%} drop)"
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force",
        action="store_true",
        help="write the output even if the safety guard would abort",
    )
    args = parser.parse_args(argv)

    print("=" * 62)
    print("Dev Remote Jobs Crawler")
    print("=" * 62)

    jobs = get_all_jobs()

    problem = guard(jobs, args.force)
    if problem:
        print(f"[!] ABORTED: {problem}. Existing data left untouched.")
        print("    Re-run with --force only if this is expected.")
        return 1

    stats = build_stats(jobs)
    write_json(JOBS_PATH, jobs)
    write_json(STATS_PATH, stats)
    write_feed(jobs)
    readme_updated = update_readme(jobs, stats)

    print(f"[*] data/jobs.json  -> {len(jobs)} listings")
    print(f"[*] data/feed.xml   -> {min(len(jobs), 100)} items")
    print(
        f"[*] data/stats.json -> {stats['salary_coverage']}% salary coverage, "
        f"sources: {', '.join(f'{k} ({v})' for k, v in stats['sources'].items())}"
    )
    print(f"[*] README.md       -> {'updated' if readme_updated else 'unchanged'}")
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
