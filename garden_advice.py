
"""
garden_advice.py
A simple script that gives gardening tips.
"""

# TODO: Refactor into a function called get_garden_advice() that returns
# advice instead of just printing
# TODO: Replace hardcoded advice with a dictionary that gives tips based on
# season/month
# TODO: Add simple unit tests for get_garden_advice()

from typing import Optional


ADVICE_BY_SEASON = {
    "spring": (
        "Start seeds indoors, prune shrubs, and prepare beds with compost."
    ),
    "summer": (
        "Water early in the morning and mulch to retain soil moisture."
    ),
    "autumn": (
        "Harvest late crops, plant cover crops, and clean up fallen leaves."
    ),
    "fall": (
        "Harvest late crops, plant cover crops, and clean up fallen leaves."
    ),
    "winter": (
        "Plan next season, protect perennials, and avoid overwatering indoors."
    ),
}


ADVICE_BY_MONTH = {
    "january": (
        "Check indoor plants for pests and plan your seed order."
    ),
    "february": (
        "Start cool-season seeds and clean/sterilize tools."
    ),
    "march": (
        "Direct sow hardy greens; begin hardening off seedlings."
    ),
    "april": (
        "Plant potatoes and onions; watch for late frosts."
    ),
    "may": (
        "Transplant warm-season crops after last frost date."
    ),
    "june": (
        "Stake tall plants and keep up with weeding."
    ),
    "july": (
        "Harvest frequently and water deeply but infrequently."
    ),
    "august": (
        "Sow fall crops like kale and radishes."
    ),
    "september": (
        "Divide perennials and start collecting seeds."
    ),
    "october": (
        "Plant garlic and add mulch to beds."
    ),
    "november": (
        "Compost fallen leaves and clean up garden debris."
    ),
    "december": (
        "Sharpen tools and map out crop rotation for spring."
    ),
}


def normalize(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    return value.strip().lower()


def get_garden_advice(
    month: Optional[str] = None, season: Optional[str] = None
) -> str:
    """
    Return gardening advice based on month or season.

    If both month and season are provided, month-specific advice is
    prioritized.
    If neither matches, a generic reminder is returned.

    Args:
        month: Name of the month (e.g., "March"). Case-insensitive.
        season: Name of the season ("spring", "summer", "autumn"/"fall",
            "winter"). Case-insensitive.

    Returns:
        A short gardening advice string.
    """
    normalized_month = normalize(month)
    normalized_season = normalize(season)

    if normalized_month and normalized_month in ADVICE_BY_MONTH:
        return ADVICE_BY_MONTH[normalized_month]

    if normalized_season and normalized_season in ADVICE_BY_SEASON:
        return ADVICE_BY_SEASON[normalized_season]

    return (
        "Remember to water your plants regularly and observe local conditions!"
    )


def _main() -> None:
    # Minimal CLI for manual use
    import argparse

    parser = argparse.ArgumentParser(
        description="Get gardening advice by month or season."
    )
    parser.add_argument(
        "--month", type=str, help="Month name, e.g. 'March'", default=None
    )
    parser.add_argument(
        "--season",
        type=str,
        help="Season name, e.g. 'spring'",
        default=None,
    )
    args = parser.parse_args()

    advice = get_garden_advice(month=args.month, season=args.season)
    print(advice)


if __name__ == "__main__":
    _main()
