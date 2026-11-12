"""
Remote developer jobs aggregator & normalizer.

Fetches high quality public feeds (RemoteOK, WeWorkRemotely, Remotive) and
turns them into one normalized schema. Standard library only: no dependencies.

The parsing functions are pure (payload in, jobs out) so they can be tested
offline with frozen fixtures. Only ``fetch_*`` touches the network.
"""

from __future__ import annotations

import hashlib
import json
import re
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from collections.abc import Sequence
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

try:  # script execution (python src/main.py) and package import both work
    from .classify import (
        DEFAULT_CATEGORY,
        clean_html,
        detect_category,
        extract_tags,
        is_dev_job,
        normalize,
        shorten,
    )
except ImportError:  # pragma: no cover
    from classify import (  # type: ignore[no-redef]
        DEFAULT_CATEGORY,
        clean_html,
        detect_category,
        extract_tags,
        is_dev_job,
        normalize,
        shorten,
    )

USER_AGENT = "DevRemoteJobsMonitor/2.0 (+https://github.com/LeandroCarlino/dev-remote-jobs-monitor)"
TIMEOUT = 20
MAX_PER_SOURCE = 120
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #
def fetch_url(url: str, timeout: int = TIMEOUT, retries: int = 2) -> str:
    """GET a URL as UTF-8 text, retrying transient failures once."""
    last_error: Exception | None = None
    for _ in range(retries):
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "application/json, application/xml, text/xml, */*",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read().decode("utf-8", errors="replace")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_error = exc
    raise RuntimeError(f"could not fetch {url}: {last_error}")


# --------------------------------------------------------------------------- #
# Normalization helpers
# --------------------------------------------------------------------------- #
def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _iso_date(value: str | None) -> str:
    """Validate an already-ISO date, otherwise fall back to today."""
    candidate = (value or "").strip()[:10]
    return candidate if DATE_RE.match(candidate) else _today()


def _epoch_date(epoch: object) -> str:
    try:
        return datetime.fromtimestamp(int(epoch), tz=timezone.utc).strftime("%Y-%m-%d")
    except (TypeError, ValueError, OSError, OverflowError):
        return _today()


def _rfc822_date(value: str | None) -> str:
    try:
        return (
            parsedate_to_datetime(value or "")
            .astimezone(timezone.utc)
            .strftime("%Y-%m-%d")
        )
    except (TypeError, ValueError):
        return _today()


def _money(value: object) -> int | None:
    try:
        amount = int(float(str(value).replace(",", "")))
    except (TypeError, ValueError):
        return None
    return amount if amount > 0 else None


def format_salary(low: object = None, high: object = None) -> str | None:
    """Build a compact salary string from a min/max pair."""
    low_value, high_value = _money(low), _money(high)
    if low_value and high_value and low_value != high_value:
        return f"${low_value:,} - ${high_value:,} USD"
    single = low_value or high_value
    return f"${single:,}+ USD" if single else None


def job_id(url: str, title: str, company: str) -> str:
    key = url.strip() or f"{normalize(title)}|{normalize(company)}"
    return hashlib.md5(key.encode("utf-8")).hexdigest()[:12]


def build_job(
    *,
    title: str,
    company: str,
    url: str,
    location: str,
    date: str,
    tags: list[str],
    salary: str | None,
    source: str,
    hints: Sequence[str] | None = None,
) -> dict:
    """Assemble one listing with the canonical schema (stable for API users)."""
    clean_title = shorten(clean_html(title), 140) or "Untitled role"
    clean_company = shorten(clean_html(company), 80) or "Unknown"
    clean_url = (url or "").strip()
    return {
        "id": job_id(clean_url, clean_title, clean_company),
        "title": clean_title,
        "company": clean_company,
        "url": clean_url if clean_url.startswith("http") else "",
        "location": shorten(clean_html(location), 80) or "Remote",
        "date": date,
        "category": detect_category(clean_title, tags, hints) or DEFAULT_CATEGORY,
        "tags": tags,
        "salary": salary,
        "source": source,
    }


def _count_items(payload: object) -> int:
    if isinstance(payload, list):
        return sum(
            1 for item in payload if isinstance(item, dict) and "legal" not in item
        )
    return 0


# --------------------------------------------------------------------------- #
# RemoteOK
# --------------------------------------------------------------------------- #
def parse_remoteok(payload: object) -> list[dict]:
    """Normalize the RemoteOK /api payload, dropping non-dev listings."""
    if not isinstance(payload, list):
        return []

    jobs: list[dict] = []
    for item in payload:
        if not isinstance(item, dict) or "legal" in item:
            continue

        title = clean_html(item.get("position") or "")
        if not title:
            continue

        seed_tags = item.get("tags") or []
        if not is_dev_job(title, seed_tags):
            continue

        tags = extract_tags(title, seed_tags)

        url = (item.get("apply_url") or item.get("url") or "").strip()
        if url and not url.startswith("http"):
            url = "https://remoteok.com" + url
        if not url:
            continue

        jobs.append(
            build_job(
                title=title,
                company=item.get("company") or "Unknown",
                url=url,
                location=item.get("location") or "Worldwide Remote",
                date=_epoch_date(item.get("epoch")) if item.get("epoch") else _today(),
                tags=tags,
                salary=format_salary(item.get("salary_min"), item.get("salary_max")),
                source="RemoteOK",
                hints=seed_tags,
            )
        )
        if len(jobs) >= MAX_PER_SOURCE:
            break

    return jobs


def fetch_remoteok() -> tuple[list[dict], int]:
    payload = json.loads(fetch_url("https://remoteok.com/api"))
    jobs = parse_remoteok(payload)
    return jobs, _count_items(payload) - len(jobs)


# --------------------------------------------------------------------------- #
# WeWorkRemotely (RSS)
# --------------------------------------------------------------------------- #
WWR_FEEDS = (
    "https://weworkremotely.com/categories/remote-programming-jobs.rss",
    "https://weworkremotely.com/categories/remote-devops-sysadmin-jobs.rss",
)


def parse_weworkremotely(xml_text: str) -> list[dict]:
    """Normalize one WeWorkRemotely RSS feed ("Company: Role" titles)."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return []

    channel = root.find("channel")
    if channel is None:
        return []

    jobs: list[dict] = []
    for item in channel.findall("item"):
        title_full = clean_html(item.findtext("title") or "")
        link = (item.findtext("link") or "").strip()
        if not title_full or not link:
            continue

        company, _, position = title_full.partition(":")
        if not position.strip():
            company, position = "WeWorkRemotely", title_full
        position = position.strip()

        tags = extract_tags(position)
        if not is_dev_job(position):
            continue

        jobs.append(
            build_job(
                title=position,
                company=company.strip() or "WeWorkRemotely",
                url=link,
                location="Worldwide / Remote",
                date=_rfc822_date(item.findtext("pubDate")),
                tags=tags,
                salary=None,
                source="WeWorkRemotely",
            )
        )
        if len(jobs) >= MAX_PER_SOURCE:
            break

    return jobs


def fetch_weworkremotely() -> tuple[list[dict], int]:
    jobs: list[dict] = []
    for feed_url in WWR_FEEDS:
        try:
            xml_text = fetch_url(feed_url)
        except RuntimeError as exc:
            print(f"[!] WeWorkRemotely feed failed ({feed_url}): {exc}")
            continue
        jobs.extend(parse_weworkremotely(xml_text))
    # These feeds are already dev-only, so there is no drop counter to report.
    return jobs, 0


# --------------------------------------------------------------------------- #
# Remotive
# --------------------------------------------------------------------------- #
REMOTIVE_URL = "https://remotive.com/api/remote-jobs?category=software-dev&limit=100"


def parse_remotive(payload: object) -> list[dict]:
    """Normalize the Remotive API payload (already software-dev only)."""
    if not isinstance(payload, dict):
        return []

    jobs: list[dict] = []
    for item in payload.get("jobs") or []:
        if not isinstance(item, dict):
            continue

        title = clean_html(item.get("title") or "")
        url = (item.get("url") or "").strip()
        if not title or not url:
            continue

        seed_tags = item.get("tags") or []
        if not is_dev_job(title, seed_tags):
            continue

        tags = extract_tags(title, seed_tags)

        salary = (item.get("salary") or "").strip()
        jobs.append(
            build_job(
                title=title,
                company=item.get("company_name") or "Unknown",
                url=url,
                location=item.get("candidate_required_location") or "Worldwide",
                date=_iso_date(str(item.get("publication_date") or "")),
                tags=tags,
                salary=salary or None,
                source="Remotive",
                hints=seed_tags,
            )
        )
        if len(jobs) >= MAX_PER_SOURCE:
            break

    return jobs


def fetch_remotive() -> tuple[list[dict], int]:
    payload = json.loads(fetch_url(REMOTIVE_URL))
    jobs = parse_remotive(payload)
    total = len(payload.get("jobs") or []) if isinstance(payload, dict) else 0
    return jobs, total - len(jobs)


# --------------------------------------------------------------------------- #
# Aggregation
# --------------------------------------------------------------------------- #
def dedupe(jobs: list[dict]) -> list[dict]:
    """Drop duplicates by URL hash first, then by title+company."""
    by_id: dict[str, dict] = {}
    by_pair: set[tuple[str, str]] = set()
    for job in jobs:
        pair = (normalize(job["title"]), normalize(job["company"]))
        if job["id"] in by_id or pair in by_pair:
            continue
        by_id[job["id"]] = job
        by_pair.add(pair)
    return list(by_id.values())


def get_all_jobs() -> list[dict]:
    """Fetch every source, normalize, filter and sort newest first."""
    collectors = (
        ("RemoteOK", fetch_remoteok),
        ("WeWorkRemotely", fetch_weworkremotely),
        ("Remotive", fetch_remotive),
    )

    collected: list[dict] = []
    for name, collector in collectors:
        try:
            jobs, dropped = collector()
        except Exception as exc:  # one broken source must not kill the run
            print(f"[!] {name} failed: {exc}")
            continue
        print(f"[*] {name}: {len(jobs)} dev listings kept, {max(dropped, 0)} dropped")
        collected.extend(jobs)

    jobs = dedupe(collected)
    jobs.sort(key=lambda job: (job["date"], job["title"]), reverse=True)
    print(f"[*] {len(jobs)} unique listings after de-duplication")
    return jobs
