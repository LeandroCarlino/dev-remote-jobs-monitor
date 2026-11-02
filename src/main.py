"""
Main script for dev-remote-jobs-monitor
Runs crawler, writes data/jobs.json and updates README.md
"""

import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.fetcher import get_all_jobs

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")
WEB_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "web", "data")

def generate_markdown_table(jobs: list[dict], limit: int = 30) -> str:
    lines = [
        "| Puesto | Empresa | Categoría | Tags | Ubicación | Fecha |",
        "|:-------|:--------|:----------|:-----|:----------|:------|"
    ]

    for j in jobs[:limit]:
        title = j.get("title", "").replace("|", "-")
        company = j.get("company", "").replace("|", "-")
        url = j.get("url", "#")
        category = j.get("category", "General")
        tags_list = j.get("tags", [])
        tags_str = " ".join([f"`{t}`" for t in tags_list[:3]]) if tags_list else "-"
        location = j.get("location", "Remote").replace("|", "-")
        if len(location) > 22:
            location = location[:20] + "…"
        date_str = j.get("date", "")

        link_md = f"[{title}]({url})"
        lines.append(f"| **{link_md}** | {company} | `{category}` | {tags_str} | {location} | {date_str} |")

    return "\n".join(lines)

def update_readme(jobs: list[dict], stats: dict):
    if not os.path.exists(README_PATH):
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    table_md = generate_markdown_table(jobs, limit=25)

    # Replace jobs section
    start_tag = "<!-- JOBS_START -->"
    end_tag = "<!-- JOBS_END -->"
    if start_tag in content and end_tag in content:
        prefix = content.split(start_tag)[0] + start_tag + "\n"
        suffix = "\n" + end_tag + content.split(end_tag)[1]
        content = prefix + f"\n*Última actualización automática: **{now_utc}** | Ofertas activas monitoreadas: **{len(jobs)}***\n\n" + table_md + suffix

    # Replace stats section
    stats_start = "<!-- STATS_START -->"
    stats_end = "<!-- STATS_END -->"
    if stats_start in content and stats_end in content:
        top_tags = stats.get("top_tags", {})
        badges = " ".join([f"![{tag}](https://img.shields.io/badge/{tag}-{count}_vacantes-indigo)" for tag, count in list(top_tags.items())[:8]])
        stats_block = f"\n### 📊 Tecnologías con más demanda hoy\n\n{badges}\n"
        prefix = content.split(stats_start)[0] + stats_start
        suffix = stats_end + content.split(stats_end)[1]
        content = prefix + stats_block + "\n" + suffix

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    print("=" * 60)
    print("Starting Dev Remote Jobs Crawler...")
    print("=" * 60)

    jobs = get_all_jobs()
    print(f"[*] Total unique jobs gathered: {len(jobs)}")

    # Calculate statistics
    all_tags = [t for j in jobs for t in j.get("tags", [])]
    tag_counts = dict(Counter(all_tags).most_common(20))

    categories = [j.get("category", "General") for j in jobs]
    cat_counts = dict(Counter(categories))

    stats = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "total_jobs": len(jobs),
        "top_tags": tag_counts,
        "categories": cat_counts
    }

    # Save to data directory
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(os.path.join(DATA_DIR, "jobs.json"), "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2, ensure_ascii=False)
    with open(os.path.join(DATA_DIR, "stats.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

    # Also mirror into web/data for local testing
    os.makedirs(WEB_DATA_DIR, exist_ok=True)
    with open(os.path.join(WEB_DATA_DIR, "jobs.json"), "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2, ensure_ascii=False)
    with open(os.path.join(WEB_DATA_DIR, "stats.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

    print("[*] JSON files successfully written.")

    update_readme(jobs, stats)
    print("[*] README.md updated.")
    print("Done!")

if __name__ == "__main__":
    main()
