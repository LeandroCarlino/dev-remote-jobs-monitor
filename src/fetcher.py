"""
Remote Developer Jobs Aggregator & Normalizer
Fetches from high quality public feeds (RemoteOK, WeWorkRemotely, Remotive)
Standard library only: requires no third-party dependencies!
"""

import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import hashlib

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) RemoteJobsMonitor/1.0"

TECH_TAGS = [
    "python", "javascript", "typescript", "react", "next.js", "vue", "angular",
    "node", "django", "fastapi", "flask", "go", "golang", "rust", "java", "spring",
    "c#", ".net", "php", "laravel", "ruby", "rails", "sql", "postgres", "mongodb",
    "aws", "gcp", "azure", "docker", "kubernetes", "graphql", "tailwind", "ai",
    "machine learning", "flutter", "react native", "swift", "kotlin", "devops"
]

def fetch_url(url: str, timeout: int = 15) -> str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "application/json, application/xml, text/xml, */*"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="ignore")

def extract_tags(text: str) -> list[str]:
    lowered = text.lower()
    matched = []
    for tag in TECH_TAGS:
        pattern = r"\b" + re.escape(tag) + r"\b"
        if re.search(pattern, lowered):
            matched.append(tag.capitalize() if len(tag) > 2 else tag.upper())
    return list(dict.fromkeys(matched))[:6]

def detect_category(title: str, tags: list[str]) -> str:
    combined = (title + " " + " ".join(tags)).lower()
    if any(k in combined for k in ["ai", "machine learning", "data science", "llm", "data engineer"]):
        return "AI / Data"
    if any(k in combined for k in ["devops", "sre", "cloud", "infrastructure", "kubernetes", "aws", "platform"]):
        return "DevOps / Cloud"
    if any(k in combined for k in ["frontend", "front-end", "react", "vue", "angular", "ui/ux", "web"]):
        return "Frontend"
    if any(k in combined for k in ["backend", "back-end", "django", "fastapi", "golang", "go ", "spring", "rails", "node"]):
        return "Backend"
    if any(k in combined for k in ["mobile", "ios", "android", "flutter", "react native", "swift", "kotlin"]):
        return "Mobile"
    return "Fullstack"

def fetch_weworkremotely() -> list[dict]:
    feeds = [
        "https://weworkremotely.com/categories/remote-programming-jobs.rss",
        "https://weworkremotely.com/categories/remote-devops-sysadmin-jobs.rss",
    ]
    jobs = []
    for feed_url in feeds:
        try:
            xml_text = fetch_url(feed_url)
            root = ET.fromstring(xml_text)
            channel = root.find("channel")
            if channel is None:
                continue
            for item in channel.findall("item"):
                title_elem = item.find("title")
                link_elem = item.find("link")
                pub_elem = item.find("pubDate")
                desc_elem = item.find("description")

                title_full = title_elem.text if title_elem is not None and title_elem.text else ""
                link = link_elem.text if link_elem is not None and link_elem.text else ""
                pub_date = pub_elem.text if pub_elem is not None and pub_elem.text else ""
                desc = desc_elem.text if desc_elem is not None and desc_elem.text else ""

                # Format in WWR is often: "Company: Job Title"
                company = "WeWorkRemotely"
                position = title_full
                if ":" in title_full:
                    parts = title_full.split(":", 1)
                    company = parts[0].strip()
                    position = parts[1].strip()

                iso_date = ""
                if pub_date:
                    try:
                        iso_date = parsedate_to_datetime(pub_date).astimezone(timezone.utc).strftime("%Y-%m-%d")
                    except Exception:
                        iso_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

                tags = extract_tags(position + " " + desc[:1000])
                category = detect_category(position, tags)

                job_id = hashlib.md5((link or position + company).encode("utf-8")).hexdigest()[:12]
                jobs.append({
                    "id": job_id,
                    "title": position,
                    "company": company,
                    "url": link,
                    "location": "Worldwide / Remote",
                    "date": iso_date,
                    "category": category,
                    "tags": tags,
                    "salary": None,
                    "source": "WeWorkRemotely"
                })
        except Exception as e:
            print(f"[!] Warning fetching WWR ({feed_url}): {e}")
    return jobs

def fetch_remoteok() -> list[dict]:
    url = "https://remoteok.com/api"
    jobs = []
    try:
        raw_json = fetch_url(url)
        data = json.loads(raw_json)
        # First element is legal disclaimer in RemoteOK
        items = data[1:] if len(data) > 1 and isinstance(data, list) else []
        for item in items[:40]:
            position = item.get("position", "")
            company = item.get("company", "Unknown")
            apply_url = item.get("url", "")
            if not apply_url.startswith("http"):
                apply_url = f"https://remoteok.com{apply_url}"

            raw_tags = item.get("tags", [])
            extracted = extract_tags(" ".join(raw_tags) + " " + position)
            tags = list(dict.fromkeys([t.capitalize() for t in raw_tags if len(t) <= 15] + extracted))[:6]

            epoch = item.get("epoch")
            iso_date = datetime.fromtimestamp(epoch, tz=timezone.utc).strftime("%Y-%m-%d") if epoch else datetime.now(timezone.utc).strftime("%Y-%m-%d")

            location = item.get("location") or "Worldwide Remote"
            salary_min = item.get("salary_min")
            salary_max = item.get("salary_max")
            salary_str = f"${salary_min:,} - ${salary_max:,} USD" if salary_min and salary_max else None

            job_id = hashlib.md5((apply_url or position + company).encode("utf-8")).hexdigest()[:12]
            jobs.append({
                "id": job_id,
                "title": position,
                "company": company,
                "url": apply_url,
                "location": location,
                "date": iso_date,
                "category": detect_category(position, tags),
                "tags": tags,
                "salary": salary_str,
                "source": "RemoteOK"
            })
    except Exception as e:
        print(f"[!] Warning fetching RemoteOK: {e}")
    return jobs

def fetch_remotive() -> list[dict]:
    url = "https://remotive.com/api/remote-jobs?category=software-dev&limit=40"
    jobs = []
    try:
        raw_json = fetch_url(url)
        data = json.loads(raw_json)
        for item in data.get("jobs", []):
            position = item.get("title", "")
            company = item.get("company_name", "")
            apply_url = item.get("url", "")
            pub_date = item.get("publication_date", "")[:10]
            candidate_loc = item.get("candidate_required_location") or "Worldwide"
            salary_str = item.get("salary") or None
            raw_tags = item.get("tags", [])
            tags = extract_tags(" ".join(raw_tags) + " " + position)

            job_id = hashlib.md5((apply_url or position + company).encode("utf-8")).hexdigest()[:12]
            jobs.append({
                "id": job_id,
                "title": position,
                "company": company,
                "url": apply_url,
                "location": candidate_loc,
                "date": pub_date,
                "category": detect_category(position, tags),
                "tags": tags,
                "salary": salary_str if salary_str and salary_str.strip() else None,
                "source": "Remotive"
            })
    except Exception as e:
        print(f"[!] Warning fetching Remotive: {e}")
    return jobs

def get_all_jobs() -> list[dict]:
    all_jobs = []
    print("[*] Fetching RemoteOK jobs...")
    all_jobs.extend(fetch_remoteok())

    print("[*] Fetching WeWorkRemotely jobs...")
    all_jobs.extend(fetch_weworkremotely())

    print("[*] Fetching Remotive jobs...")
    all_jobs.extend(fetch_remotive())

    # Deduplicate by url or title+company
    unique_jobs = {}
    for job in all_jobs:
        key = (job["title"].strip().lower(), job["company"].strip().lower())
        if key not in unique_jobs:
            unique_jobs[key] = job

    # Sort descending by date
    sorted_jobs = sorted(unique_jobs.values(), key=lambda j: j.get("date", ""), reverse=True)
    return sorted_jobs
