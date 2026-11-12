"""Unit tests for the classification rules (tags, categories, dev filter)."""

from __future__ import annotations

import unittest

from src.classify import (
    DEFAULT_CATEGORY,
    clean_html,
    detect_category,
    extract_tags,
    is_dev_job,
    shorten,
)


class ExtractTagsTest(unittest.TestCase):
    def test_keeps_known_seed_tags_and_drops_noise(self):
        tags = extract_tags(
            "Registered Nurse",
            seed_tags=["Medical", "Travel", "Education", "python"],
        )
        self.assertEqual(tags, ["Python"])

    def test_matches_dotted_and_hashed_technologies(self):
        tags = extract_tags("Looking for C# and .NET developers with Next.js")
        self.assertIn("C#", tags)
        self.assertIn(".NET", tags)
        self.assertIn("Next.js", tags)

    def test_go_requires_capitalisation(self):
        self.assertEqual(extract_tags("Go developer for our platform"), ["Go"])
        self.assertEqual(extract_tags("go to market strategy"), [])

    def test_no_duplicate_display_names(self):
        tags = extract_tags("Golang and Go services", seed_tags=["go"])
        self.assertEqual(tags, ["Go"])

    def test_limit_is_respected(self):
        tags = extract_tags(
            "python javascript typescript react vue angular rust java sql aws"
        )
        self.assertEqual(len(tags), 5)


class DetectCategoryTest(unittest.TestCase):
    def test_fullstack_wins_over_frontend(self):
        self.assertEqual(
            detect_category("Full Stack Developer (React, Node)", ["React"]),
            "Fullstack",
        )

    def test_substring_bug_is_gone(self):
        # "paid" / "email" used to match the bare "ai" substring rule.
        self.assertNotEqual(
            detect_category("Paid Media Manager US", ["Marketing"]), "AI / Data"
        )
        self.assertNotEqual(detect_category("Email Marketing Specialist"), "AI / Data")
        self.assertNotEqual(detect_category("Web3 Business Development"), "Frontend")

    def test_ai_and_data_roles(self):
        self.assertEqual(
            detect_category("Senior Machine Learning Engineer", ["Python"]), "AI / Data"
        )
        self.assertEqual(detect_category("Data Engineer", ["SQL"]), "AI / Data")

    def test_devops_and_cloud(self):
        self.assertEqual(
            detect_category(
                "Senior Software Engineer — Kubernetes Control Plane", ["Golang"]
            ),
            "DevOps / Cloud",
        )

    def test_mobile_before_frontend(self):
        self.assertEqual(detect_category("React Native Developer"), "Mobile")

    def test_unknown_falls_back_to_general_not_fullstack(self):
        self.assertEqual(detect_category("Technical Writer"), DEFAULT_CATEGORY)
        self.assertEqual(DEFAULT_CATEGORY, "General")

    def test_source_hints_disambiguate_generic_titles(self):
        self.assertEqual(
            detect_category("Staff Software Engineer", ["Python"], ["backend"]),
            "Backend",
        )
        self.assertEqual(
            detect_category("Staff Software Engineer", [], ["front end"]),
            "Frontend",
        )

    def test_title_beats_hints(self):
        self.assertEqual(
            detect_category("Mobile Engineer", [], ["backend"]),
            "Mobile",
        )


class IsDevJobTest(unittest.TestCase):
    CASES = (
        ("Senior Python Engineer", ["dev"], True),
        ("Data Engineer", ["data"], True),
        ("Cloud Engineer", ["engineer"], True),
        ("Head of Technology", [], True),
        ("Systems Integrator", ["Dev", "Software"], True),
        ("Registered Nurse", ["medical"], False),
        ("Accountant", ["finance"], False),
        ("Recruiting Coordinator", [], False),
        ("Paid Media Manager US", ["Marketing"], False),
        ("Web3 Business Development", ["Crypto"], False),
        ("Bilingual Patient Engagement Specialist", ["Dev", "Speech"], False),
        ("HIL Support Specialist", ["Dev", "C sharp"], False),
        ("Support Specialist", [], False),
        ("Director of Product Management and IT Operations", ["Security"], False),
        ("", [], False),
    )

    def test_filter_matrix(self):
        for title, seeds, expected in self.CASES:
            with self.subTest(title=title):
                self.assertIs(is_dev_job(title, seeds), expected, title)


class ShortenTest(unittest.TestCase):
    def test_short_text_is_untouched(self):
        self.assertEqual(shorten("Backend Engineer", 40), "Backend Engineer")

    def test_long_text_is_cut_on_a_word_boundary(self):
        result = shorten("Senior Software Engineer with Kubernetes experience", 20)
        self.assertLessEqual(len(result), 20)
        self.assertTrue(result.endswith("\u2026"))
        self.assertNotIn("Kuber", result)


class CleanHtmlTest(unittest.TestCase):
    def test_tags_and_entities_are_removed(self):
        self.assertEqual(clean_html("<p>AI &amp; <b>ML</b></p>"), "AI & ML")

    def test_double_encoded_upstream_text_is_repaired(self):
        # RemoteOK sometimes returns "Senior Engineer â€” Remote".
        broken = "Senior Engineer \u00e2\u0080\u0094 Kubernetes"
        self.assertEqual(clean_html(broken), "Senior Engineer \u2014 Kubernetes")

    def test_correct_text_is_left_alone(self):
        self.assertEqual(clean_html("Diseñador — remoto"), "Diseñador — remoto")


if __name__ == "__main__":
    unittest.main()
