"""
Basic unit tests for garden_advice.get_garden_advice
"""

import unittest

from garden_advice import get_garden_advice


class TestGardenAdvice(unittest.TestCase):
    def test_spring_advice(self):
        result = get_garden_advice("spring")
        self.assertIn("roses", result)

    def test_summer_advice(self):
        result = get_garden_advice("summer")
        self.assertIn("Water deeply", result)

    def test_autumn_advice(self):
        result = get_garden_advice("autumn")
        self.assertIn("Harvest vegetables", result)

    def test_winter_advice(self):
        result = get_garden_advice("winter")
        self.assertIn("frost", result)

    def test_unknown_season_returns_fallback(self):
        result = get_garden_advice("unknown")
        self.assertEqual("No advice available for this season.", result)

    def test_case_insensitive_season(self):
        result_upper = get_garden_advice("SPRING")
        result_lower = get_garden_advice("spring")
        self.assertEqual(result_upper, result_lower)


if __name__ == "__main__":
    unittest.main()