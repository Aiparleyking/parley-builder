# vip_system.py

def is_vip_pick(player_data):
    """
    Determine if a player qualifies as a VIP pick based on their boosts.

    Args:
        player_data (dict): Player info and boost status.

    Returns:
        bool: True if player is VIP, False otherwise.
    """

    score = 0

    if player_data.get('CorePassed', False):
        score += 1

    if player_data.get('WeatherBoost', '') == 'Good':
        score += 1

    if player_data.get('BallparkBoost', '') == 'Good':
        score += 1

    # If the player passes at least 2 out of 3 (core, weather, ballpark) ➔ VIP
    return score >= 2
