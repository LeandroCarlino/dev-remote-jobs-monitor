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
        detect_region,
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
        detect_region,
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


def format_salary(
    low: object = None,
    high: object = None,
    currency: str | None = "USD",
) -> str | None:
    """Build a compact salary string from a min/max pair."""
    low_value, high_value = _money(low), _money(high)
    suffix = f" {currency}" if currency else ""
    if low_value and high_value and low_value != high_value:
        return f"${low_value:,} - ${high_value:,}{suffix}"
    single = low_value or high_value
    return f"${single:,}+{suffix}" if single else None


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
    region: str | None = None,
) -> dict:
    """Assemble one listing with the canonical schema (stable for API users)."""
    clean_title = shorten(clean_html(title), 140) or "Untitled role"
    clean_company = shorten(clean_html(company), 80) or "Unknown"
    clean_url = (url or "").strip()
    clean_location = shorten(clean_html(location), 80) or "Remote"
    return {
        "id": job_id(clean_url, clean_title, clean_company),
        "title": clean_title,
        "company": clean_company,
        "url": clean_url if clean_url.startswith("http") else "",
        "location": clean_location,
        "region": region or detect_region(clean_location),
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
# Get on Board (LATAM tech job board)
# --------------------------------------------------------------------------- #
GETONBRD_URL = (
    "https://www.getonbrd.com/api/v0/categories/programming/jobs"
    "?per_page=120&expand[]=company&page={page}"
)
GETONBRD_MAX_PAGES = 3
GETONBRD_LIMIT = 200

# Get on Board returns snake_case modalities, which look broken in a UI.
MODALITY_LABELS = {
    "fully_remote": "Fully remote",
    "remote_local": "Remote (local)",
    "remote": "Remote",
    "hybrid": "Hybrid",
    "on_site": "On-site",
    "onsite": "On-site",
    "part_remote": "Part remote",
}


def _modality_label(value: str) -> str:
    cleaned = (value or "").strip().lower()
    if not cleaned:
        return ""
    return MODALITY_LABELS.get(cleaned, cleaned.replace("_", " ").capitalize())


def _getonbrd_company(attributes: dict) -> str:
    company = attributes.get("company") or {}
    data = company.get("data") if isinstance(company, dict) else None
    if isinstance(data, dict):
        return ((data.get("attributes") or {}).get("name")) or "Unknown"
    return "Unknown"


def parse_getonbrd(payload: object) -> list[dict]:
    """Normalize a Get on Board API page (LATAM-focused tech board)."""
    if not isinstance(payload, dict):
        return []

    jobs: list[dict] = []
    for item in payload.get("data") or []:
        if not isinstance(item, dict):
            continue
        attributes = item.get("attributes") or {}
        title = clean_html(attributes.get("title") or "")
        slug = (item.get("id") or "").strip()
        if not title or not slug:
            continue
        if not is_dev_job(title):
            continue

        countries = [
            country for country in attributes.get("countries") or [] if country
        ]
        modality = _modality_label(attributes.get("remote_modality") or "")
        if not modality and attributes.get("remote"):
            modality = "Remote"
        location = ", ".join(countries) or (
            "Remote" if attributes.get("remote") else "Latam"
        )
        if modality:
            location = f"{location} · {modality}"

        # The board is Latam-only, so "Remote" there means remote within Latam.
        detected = detect_region(location)
        region = "latam" if detected in {"other", "worldwide"} else detected

        jobs.append(
            build_job(
                title=title,
                company=_getonbrd_company(attributes),
                url=f"https://www.getonbrd.com/jobs/{slug}",
                location=location,
                date=_epoch_date(attributes.get("published_at")),
                tags=extract_tags(title),
                salary=format_salary(
                    attributes.get("min_salary"),
                    attributes.get("max_salary"),
                    currency=None,
                ),
                source="Get on Board",
                region=region,
            )
        )
        if len(jobs) >= GETONBRD_LIMIT:
            break

    return jobs


def fetch_getonbrd() -> tuple[list[dict], int]:
    jobs: list[dict] = []
    seen = 0
    for page in range(1, GETONBRD_MAX_PAGES + 1):
        payload = json.loads(fetch_url(GETONBRD_URL.format(page=page)))
        if not isinstance(payload, dict):
            break
        seen += len(payload.get("data") or [])
        jobs.extend(parse_getonbrd(payload))
        total_pages = (payload.get("meta") or {}).get("total_pages")
        if total_pages and page >= int(total_pages):
            break
        if len(jobs) >= GETONBRD_LIMIT:
            break
    return jobs[:GETONBRD_LIMIT], max(seen - len(jobs), 0)


# --------------------------------------------------------------------------- #
# Jobicy (global remote board, Latam filter)
# --------------------------------------------------------------------------- #
JOBICY_URL = "https://jobicy.com/api/v2/remote-jobs?count=100&geo=latam"


def parse_jobicy(payload: object) -> list[dict]:
    """Normalize the Jobicy API payload (already filtered to Latam-eligible)."""
    if not isinstance(payload, dict):
        return []

    jobs: list[dict] = []
    for item in payload.get("jobs") or []:
        if not isinstance(item, dict):
            continue

        title = clean_html(item.get("jobTitle") or "")
        url = (item.get("url") or "").strip()
        if not title or not url:
            continue

        industry = item.get("jobIndustry") or []
        if not is_dev_job(title, industry):
            continue

        jobs.append(
            build_job(
                title=title,
                company=item.get("companyName") or "Unknown",
                url=url,
                location=clean_html(item.get("jobGeo") or "") or "Anywhere",
                date=_iso_date(str(item.get("pubDate") or "")),
                tags=extract_tags(title),
                salary=format_salary(
                    item.get("annualSalaryMin"),
                    item.get("annualSalaryMax"),
                    currency=item.get("salaryCurrency") or "USD",
                ),
                source="Jobicy",
            )
        )
        if len(jobs) >= MAX_PER_SOURCE:
            break

    return jobs


def fetch_jobicy() -> tuple[list[dict], int]:
    payload = json.loads(fetch_url(JOBICY_URL))
    jobs = parse_jobicy(payload)
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
        ("Get on Board", fetch_getonbrd),
        ("Jobicy", fetch_jobicy),
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
