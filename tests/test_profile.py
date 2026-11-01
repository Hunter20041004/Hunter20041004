from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

FEATURED = (
    "campusward-nccu",
    "lol-video-generator",
    "daibu-content-brain",
    "hotai-ai-hackathon-2026",
    "nccu-coursework/tree/main/%E4%BB%A5%E5%89%8D/%E8%A8%AD%E8%A8%88%E6%80%9D%E8%80%83%E8%88%87%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/%E4%BD%9C%E6%A5%AD%EF%BD%9C%E6%99%BA%E6%85%A7%E7%9B%B8%E7%B0%BF%E6%95%B4%E7%90%86",
    "nccu-coursework/tree/main/115-1/%E6%99%BA%E6%85%A7%E4%BA%BA%E6%A9%9F%E4%BA%92%E5%8B%95/%E4%BD%9C%E6%A5%AD%EF%BD%9CFactoryMind%20%E4%BA%92%E5%8B%95%E7%A4%BA%E7%AF%84",
    "survey-lottery-automation",
    "nccu-coursework)",
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
        for retired in (
            "taipei-cafe-recommender-excel",
            "smart-album-cleaner/",
            "factorymind-webapp",
            "alice-rag-data",
            "microbit-anti-theft-radio",
        ):
            self.assertNotIn(retired, readme)
        self.assertNotIn("second-brain", readme)
        self.assertNotIn("hospital-digital-twin", readme)
        self.assertNotIn("onrender.com", readme)
        self.assertNotIn("mailto:", readme)
        self.assertNotIn("linkedin.com", readme.casefold())
        self.assertNotIn("Location:", readme)


if __name__ == "__main__":
    unittest.main()
