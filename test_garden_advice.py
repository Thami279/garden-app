"""
Basic unit tests for garden_advice.get_garden_advice
"""

import unittest

from garden_advice import get_garden_advice


class TestGardenAdvice(unittest.TestCase):
    def test_month_overrides_season(self):
        result = get_garden_advice(month="March", season="winter")
        self.assertIn("hardy greens", result)

    def test_season_used_when_month_missing(self):
        result = get_garden_advice(season="Spring")
        self.assertIn("seeds indoors", result)

    def test_fall_and_autumn_equivalence(self):
        result_fall = get_garden_advice(season="fall")
        result_autumn = get_garden_advice(season="autumn")
        self.assertEqual(result_fall, result_autumn)

    def test_unknown_inputs_return_generic(self):
        result = get_garden_advice(month="Smarch", season="rainy")
        self.assertIn("Remember to water your plants", result)


if __name__ == "__main__":
    unittest.main()