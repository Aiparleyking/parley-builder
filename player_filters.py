def analyze_hitter_logs(hitter_logs):
    """
    Analyze a hitter's recent logs and assign a star rating.

    Args:
        hitter_logs (DataFrame): Last 10-15 games of hitter's stats.

    Returns:
        int: Star rating (3, 4, or 5). Returns None if doesn't meet criteria.
    """
    if hitter_logs is None or hitter_logs.empty:
        return None

    # Only keep games where they had an At-Bat (exclude games they sat)
    recent_games = hitter_logs[hitter_logs['AtBats'] > 0].head(10)

    if recent_games.empty:
        return None

    # Check how many games they had at least 1 hit
    hit_games = recent_games['Hits'] >= 1
    hit_count = hit_games.sum()

    # Check if they have a hit streak (consecutive games)
    streak = 0
    max_streak = 0
    for hit in hit_games:
        if hit:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0

    # Apply rules
    if max_streak >= 5:
        return 5  # 5-star pick
    elif hit_count >= 8:
        return 4  # 4-star pick
    elif hit_count >= 7:
        return 3  # 3-star pick
    else:
        return None  # Not good enough

def analyze_pitcher_logs(pitcher_logs):
    """
    Analyze a pitcher's recent form.

    Args:
        pitcher_logs (DataFrame): Last 5-10 games of pitcher's stats.

    Returns:
        bool: True if pitcher is in good form, else False.
    """
    if pitcher_logs is None or pitcher_logs.empty:
        return False

    recent_games = pitcher_logs.head(5)

    if recent_games.empty:
        return False

    avg_strikeouts = recent_games['Strikeouts'].mean()
    avg_hits_allowed = recent_games['HitsAllowed'].mean()

    # Basic pitcher rule: High strikeouts, low hits allowed
    if avg_strikeouts >= 5 and avg_hits_allowed <= 7:
        return True
    return False

def analyze_batter_vs_pitcher(bvp_data):
    """
    Analyze batter vs pitcher history.

    Args:
        bvp_data (dict): {'AtBats': int, 'Hits': int}

    Returns:
        bool: True if good vs pitcher, else False.
    """
    if bvp_data is None:
        return False

    ab = bvp_data.get('AtBats', 0)
    hits = bvp_data.get('Hits', 0)

    if ab >= 5 and hits / ab >= 0.300:
        return True
    return False

def check_injury_status(injury_status):
    """
    Check if player is healthy.

    Args:
        injury_status (str): "Healthy", "Injured", or "Unknown".

    Returns:
        bool: True if healthy, else False.
    """
    return injury_status == "Healthy"

def check_team_form(team_form, losing_streak):
    """
    Check if the player's team is playing well.

    Args:
        team_form (dict): {'Wins': int, 'Losses': int}
        losing_streak (int): Number of consecutive losses

    Returns:
        bool: True if team is above .500 and not on bad streak, else False.
    """
    wins = team_form.get('Wins', 0)
    losses = team_form.get('Losses', 0)

    if wins + losses == 0:
        return False

    winning_percentage = wins / (wins + losses)

    if winning_percentage >= 0.500 and losing_streak <= 5:
        return True
    return False
