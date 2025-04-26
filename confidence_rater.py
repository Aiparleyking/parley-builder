# confidence_rater.py

def rate_confidence(player_data):
    """
    Rates a player's or parlay's confidence from 1 to 5 stars based on boosts.

    Args:
        player_data (dict): Information about player including boost status.

    Returns:
        int: Confidence rating (1 to 5)
    """

    score = 0

    if player_data.get('CorePassed', False):
        score += 2  # Core passed is very important!

    if player_data.get('WeatherBoost', '') == 'Good':
        score += 1

    if player_data.get('BallparkBoost', '') == 'Good':
        score += 1

    if player_data.get('VIP', False):
        score += 2  # VIP players get bonus points

    # Basic system for now:
    if score <= 2:
        return 1  # ⭐
    elif score == 3:
        return 2  # ⭐⭐
    elif score == 4:
        return 3  # ⭐⭐⭐
    elif score == 5:
        return 4  # ⭐⭐⭐⭐
    else:
        return 5  # ⭐⭐⭐⭐⭐
