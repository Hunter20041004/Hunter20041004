from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

FEATURED = (
    "campusward-nccu",
    "lol-video-generator",
    "hotai-ai-hackathon-2026",
    "smart-album-cleaner",
    "factorymind-webapp",
    "survey-lottery-automation",
)


class ProfileContractTests(unittest.TestCase):
    def test_python_test_artifacts_are_ignored(self):
        gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("__pycache__/", gitignore.splitlines())
        self.assertIn("*.py[cod]", gitignore.splitlines())

    def test_profile_has_exact_identity_and_featured_project_order(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Hunter Tseng（曾尉庭）", readme)
        self.assertIn("政大會計系 ｜ Building Campusward", readme)

        positions = []
        for repository in FEATURED:
            url = f"https://github.com/Hunter20041004/{repository}"
            self.assertEqual(1, readme.count(url), repository)
            positions.append(readme.index(url))
        self.assertEqual(sorted(positions), positions)

    def test_profile_skips_retired_repos_and_invented_contact_details(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("design-thinking-ai-portfolio", readme)
        self.assertNotIn("taipei-cafe-recommender-excel", readme)
        self.assertNotIn("second-brain", readme)
        self.assertNotIn("hospital-digital-twin", readme)
        self.assertNotIn("onrender.com", readme)
        self.assertNotIn("mailto:", readme)
        self.assertNotIn("linkedin.com", readme.casefold())
        self.assertNotIn("Location:", readme)


if __name__ == "__main__":
    unittest.main()
