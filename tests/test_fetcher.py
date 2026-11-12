"""Offline tests for the fetchers, dedupe, guard and README rendering."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
import xml.etree.ElementTree as ET
from unittest import mock

from src import main as pipeline
from src.fetcher import (
    dedupe,
    format_salary,
    parse_getonbrd,
    parse_jobicy,
    parse_remotive,
    parse_remoteok,
    parse_weworkremotely,
)

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")


def load_fixture(name: str):
    path = os.path.join(FIXTURES, name)
    with open(path, encoding="utf-8") as handle:
        return handle.read() if name.endswith((".xml",)) else json.load(handle)


class RemoteOkParsingTest(unittest.TestCase):
    def setUp(self):
        self.jobs = parse_remoteok(load_fixture("remoteok.json"))

    def test_non_dev_listings_are_dropped(self):
        titles = [job["title"] for job in self.jobs]
        self.assertEqual(len(self.jobs), 5)
        for dropped in (
            "Registered Nurse",
            "Accountant",
            "Paid Media Manager US",
            "HIL Support Specialist",
        ):
            self.assertNotIn(dropped, titles)

    def test_salary_is_formatted(self):
        by_title = {job["title"]: job for job in self.jobs}
        self.assertEqual(
            by_title["Senior Python Engineer"]["salary"], "$90,000 - $130,000 USD"
        )
        self.assertEqual(by_title["Data Engineer"]["salary"], "$70,000+ USD")
        self.assertIsNone(by_title["Full Stack Developer (React, Node)"]["salary"])

    def test_categories_are_sane(self):
        by_title = {job["title"]: job for job in self.jobs}
        self.assertEqual(
            by_title["Full Stack Developer (React, Node)"]["category"], "Fullstack"
        )
        self.assertEqual(by_title["Data Engineer"]["category"], "AI / Data")
        self.assertIn("DevOps / Cloud", by_title["Senior Python Engineer"]["category"])

    def test_relative_urls_become_absolute(self):
        for job in self.jobs:
            self.assertTrue(job["url"].startswith("https://"), job["url"])

    def test_relative_apply_url_is_preferred(self):
        by_title = {job["title"]: job for job in self.jobs}
        self.assertEqual(
            by_title["Senior Python Engineer"]["url"],
            "https://remoteok.com/remote-jobs/remote-senior-python-engineer-acme-1",
        )

    def test_schema_is_stable(self):
        expected = {
            "id",
            "title",
            "company",
            "url",
            "location",
            "region",
            "date",
            "category",
            "tags",
            "salary",
            "source",
        }
        for job in self.jobs:
            self.assertEqual(set(job), expected)

    def test_ids_are_unique(self):
        self.assertEqual(len({job["id"] for job in self.jobs}), len(self.jobs))

    def test_id_is_stable_across_runs(self):
        again = parse_remoteok(load_fixture("remoteok.json"))
        self.assertEqual(
            [job["id"] for job in self.jobs],
            [job["id"] for job in again],
        )


class WeWorkRemotelyParsingTest(unittest.TestCase):
    def setUp(self):
        self.jobs = parse_weworkremotely(load_fixture("weworkremotely.xml"))

    def test_company_and_role_are_split(self):
        roles = {job["title"]: job["company"] for job in self.jobs}
        self.assertEqual(roles["Senior Rails Developer"], "Acme Corp")
        self.assertEqual(roles["DevOps Engineer"], "Big Corp")

    def test_non_dev_listing_is_dropped(self):
        titles = [job["title"] for job in self.jobs]
        self.assertEqual(len(self.jobs), 2)
        self.assertNotIn("Sales Manager", titles)

    def test_pubdate_is_converted_to_iso(self):
        by_title = {job["title"]: job for job in self.jobs}
        self.assertEqual(by_title["Senior Rails Developer"]["date"], "2026-11-11")
        self.assertEqual(by_title["DevOps Engineer"]["date"], "2026-11-10")

    def test_html_description_does_not_leak_into_tags(self):
        by_title = {job["title"]: job for job in self.jobs}
        self.assertIn("Rails", by_title["Senior Rails Developer"]["tags"])
        self.assertNotIn("<p>", by_title["Senior Rails Developer"]["tags"])

    def test_invalid_xml_returns_empty_list(self):
        self.assertEqual(parse_weworkremotely("<rss><channel>"), [])


class RemotiveParsingTest(unittest.TestCase):
    def setUp(self):
        self.jobs = parse_remotive(load_fixture("remotive.json"))

    def test_only_dev_roles_survive(self):
        titles = [job["title"] for job in self.jobs]
        self.assertEqual(len(self.jobs), 2)
        self.assertNotIn("Support Specialist", titles)

    def test_salary_and_dates(self):
        by_title = {job["title"]: job for job in self.jobs}
        self.assertEqual(
            by_title["Senior Backend Engineer"]["salary"], "$120,000 - $150,000"
        )
        self.assertEqual(by_title["Senior Backend Engineer"]["date"], "2026-11-08")

    def test_mobile_category(self):
        by_title = {job["title"]: job for job in self.jobs}
        self.assertEqual(by_title["Mobile Engineer (Flutter)"]["category"], "Mobile")


class GetOnBoardParsingTest(unittest.TestCase):
    def setUp(self):
        self.jobs = parse_getonbrd(load_fixture("getonbrd.json"))
        self.by_title = {job["title"]: job for job in self.jobs}

    def test_non_dev_listing_is_dropped(self):
        self.assertEqual(len(self.jobs), 2)
        self.assertNotIn("Product Manager", self.by_title)

    def test_company_is_expanded_from_the_relation(self):
        self.assertEqual(self.by_title["Senior Backend Engineer"]["company"], "Globex")

    def test_public_url_is_built_from_the_slug(self):
        self.assertEqual(
            self.by_title["Senior Backend Engineer"]["url"],
            "https://www.getonbrd.com/jobs/senior-backend-engineer-globex-buenos-aires",
        )

    def test_region_comes_from_the_country_list(self):
        self.assertEqual(
            self.by_title["Senior Backend Engineer"]["region"], "argentina"
        )
        self.assertEqual(
            self.by_title["Desarrollador/a Back-end Python (AWS)"]["region"],
            "latam",
        )

    def test_salary_does_not_guess_a_currency(self):
        self.assertEqual(
            self.by_title["Desarrollador/a Back-end Python (AWS)"]["salary"],
            "$2,800 - $3,000",
        )
        self.assertIsNone(self.by_title["Senior Backend Engineer"]["salary"])

    def test_location_keeps_the_modality(self):
        self.assertEqual(
            self.by_title["Senior Backend Engineer"]["location"],
            "Argentina · Remote",
        )
        self.assertEqual(
            self.by_title["Desarrollador/a Back-end Python (AWS)"]["location"],
            "Chile · Hybrid",
        )

    def test_unknown_modality_is_humanised(self):
        payload = {
            "data": [
                {
                    "id": "dev-remote-x",
                    "attributes": {
                        "title": "Backend Developer",
                        "countries": ["Chile"],
                        "remote_modality": "fully_remote",
                    },
                }
            ]
        }
        job = parse_getonbrd(payload)[0]
        self.assertEqual(job["location"], "Chile · Fully remote")

    def test_empty_payload_is_safe(self):
        self.assertEqual(parse_getonbrd({}), [])
        self.assertEqual(parse_getonbrd(None), [])


class JobicyParsingTest(unittest.TestCase):
    def setUp(self):
        self.jobs = parse_jobicy(load_fixture("jobicy.json"))
        self.by_title = {job["title"]: job for job in self.jobs}

    def test_non_dev_listing_is_dropped(self):
        self.assertEqual(len(self.jobs), 2)
        self.assertNotIn("Product Marketing Manager", self.by_title)

    def test_region_comes_from_job_geo(self):
        self.assertEqual(
            self.by_title["Senior Integration Engineer"]["region"], "latam"
        )
        self.assertEqual(self.by_title["Backend Developer"]["region"], "argentina")

    def test_salary_is_formatted_with_currency(self):
        self.assertEqual(
            self.by_title["Backend Developer"]["salary"],
            "$60,000 - $80,000 USD",
        )

    def test_date_is_trimmed_to_the_day(self):
        self.assertEqual(self.by_title["Backend Developer"]["date"], "2026-11-10")


class DedupeTest(unittest.TestCase):
    def test_duplicates_by_url_and_by_title_company(self):
        jobs = parse_remoteok(load_fixture("remoteok.json"))
        clone = dict(jobs[0])
        renamed = dict(jobs[1], id="different", url="https://example.com/other")
        merged = dedupe([*jobs, clone, renamed])
        self.assertEqual(len(merged), len(jobs))


class SalaryFormattingTest(unittest.TestCase):
    def test_formats(self):
        self.assertEqual(format_salary(80000, 120000), "$80,000 - $120,000 USD")
        self.assertEqual(format_salary(None, 120000), "$120,000+ USD")
        self.assertIsNone(format_salary(None, None))
        self.assertIsNone(format_salary("", "n/a"))


class GuardTest(unittest.TestCase):
    def test_aborts_when_too_few_listings(self):
        self.assertIsNotNone(pipeline.guard([{}] * 3, force=False))

    def test_aborts_on_a_massive_drop(self):
        with mock.patch.object(pipeline, "previous_total", return_value=100):
            self.assertIsNotNone(pipeline.guard([{}] * 30, force=False))

    def test_passes_on_a_healthy_run(self):
        with mock.patch.object(pipeline, "previous_total", return_value=100):
            self.assertIsNone(pipeline.guard([{}] * 90, force=False))

    def test_force_bypasses_the_guard(self):
        self.assertIsNone(pipeline.guard([], force=True))


class StatsTest(unittest.TestCase):
    def test_stats_shape(self):
        jobs = parse_remoteok(load_fixture("remoteok.json"))
        stats = pipeline.build_stats(jobs)
        self.assertEqual(stats["total_jobs"], len(jobs))
        self.assertEqual(set(stats["sources"]), {"RemoteOK"})
        self.assertGreater(stats["salary_coverage"], 0)
        self.assertLessEqual(stats["salary_coverage"], 100)


class FeedTest(unittest.TestCase):
    def setUp(self):
        self.jobs = parse_remoteok(load_fixture("remoteok.json"))
        self.feed = pipeline.build_feed(
            self.jobs, last_build="Wed, 12 Nov 2026 00:00:00 +0000"
        )

    def test_feed_is_valid_rss(self):
        root = ET.fromstring(self.feed)
        self.assertEqual(root.tag, "rss")
        self.assertEqual(len(root.findall("./channel/item")), len(self.jobs))
        self.assertIn("DevJobs", root.findtext("./channel/title"))

    def test_item_fields_are_usable(self):
        root = ET.fromstring(self.feed)
        item = root.findall("./channel/item")[0]
        self.assertTrue(item.findtext("link").startswith("https://"))
        self.assertRegex(item.findtext("pubDate"), r"^\w{3}, \d{2} \w{3} \d{4}")
        self.assertEqual(len(item.findtext("guid") or ""), 12)
        self.assertIsNotNone(item.findtext("description"))

    def test_special_characters_are_escaped(self):
        jobs = [
            {
                "id": "a" * 12,
                "title": "Backend & Frontend <Dev>",
                "company": "A&B",
                "url": "https://example.test/?a=1&b=2",
                "location": "Remote",
                "region": "worldwide",
                "date": "2026-11-12",
                "category": "Backend",
                "tags": ["C#"],
                "salary": None,
                "source": "Test",
            }
        ]
        feed = pipeline.build_feed(jobs)
        ET.fromstring(feed)  # would raise on malformed XML
        self.assertIn("&amp;", feed)

    def test_limit_is_respected(self):
        feed = pipeline.build_feed(self.jobs, limit=2)
        self.assertEqual(len(ET.fromstring(feed).findall("./channel/item")), 2)

    def test_invalid_date_falls_back_to_today(self):
        feed = pipeline.build_feed([{"id": "x" * 12, "title": "Dev", "date": ""}])
        item = ET.fromstring(feed).findall("./channel/item")[0]
        self.assertRegex(item.findtext("pubDate"), r"^\w{3}, \d{2} \w{3} \d{4}")


class ReadmeRenderingTest(unittest.TestCase):
    README = (
        "# Test\n\n<!-- STATS_START -->old<!-- STATS_END -->\n\n"
        "<!-- JOBS_START -->old<!-- JOBS_END -->\n"
    )

    def test_blocks_are_replaced_without_touching_the_rest(self):
        with tempfile.TemporaryDirectory() as tmp:
            readme = os.path.join(tmp, "README.md")
            with open(readme, "w", encoding="utf-8") as handle:
                handle.write(self.README)

            jobs = parse_remoteok(load_fixture("remoteok.json"))
            with mock.patch.object(pipeline, "README_PATH", readme):
                self.assertTrue(
                    pipeline.update_readme(jobs, pipeline.build_stats(jobs))
                )

            with open(readme, encoding="utf-8") as handle:
                content = handle.read()

            self.assertTrue(content.startswith("# Test"))
            self.assertNotIn("<!-- STATS_START -->old", content)
            self.assertNotIn("<!-- JOBS_START -->old", content)
            self.assertIn("Senior Python Engineer", content)
            self.assertEqual(content.count("<!-- JOBS_START -->"), 1)

    def test_missing_markers_are_reported_not_crashed(self):
        with tempfile.TemporaryDirectory() as tmp:
            readme = os.path.join(tmp, "README.md")
            with open(readme, "w", encoding="utf-8") as handle:
                handle.write("# no markers here")

            with mock.patch.object(pipeline, "README_PATH", readme):
                self.assertFalse(pipeline.update_readme([], pipeline.build_stats([])))

    def test_badge_labels_are_url_encoded(self):
        self.assertIn("C%23", pipeline._badge("C#", 3))
        self.assertIn("Machine_Learning", pipeline._badge("Machine Learning", 3))

    def test_table_dates_use_the_argentine_format(self):
        jobs = [
            {
                "title": "Backend Developer",
                "company": "Acme",
                "url": "https://example.test/job",
                "location": "Remote",
                "category": "Backend",
                "tags": ["Python"],
                "date": "2026-11-12",
                "salary": None,
                "source": "Test",
            }
        ]
        table = pipeline.generate_markdown_table(jobs)
        self.assertIn("12/11/2026", table)
        self.assertNotIn("2026-11-12", table)


if __name__ == "__main__":
    unittest.main()
