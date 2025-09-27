def get_garden_advice(season):
    """
    Returns gardening advice based on the season.
    """
    advice = {
        "spring": "Prune your roses and plant seeds!",
        "summer": "Water deeply and mulch to retain moisture.",
        "autumn": "Harvest vegetables and prepare soil for winter.",
        "winter": "Protect plants from frost and plan next season."
    }
    return advice.get(season, "No advice available for this season.")

if __name__ == "__main__":
    print(get_garden_advice("spring"))
    print(get_garden_advice("summer"))
    print(get_garden_advice("autumn"))
    print(get_garden_advice("winter"))
    print(get_garden_advice("unknown"))  # Test fallback
