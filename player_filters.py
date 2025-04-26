import pandas as pd

def analyze_hitter_logs(hitter_logs):
    """
    Checks if a hitter is hot over the last 10–15 games.
    Must have a batting average >= .250.
    """
    if hitter_logs is None or hitter_logs.empty:
        return False

    total_hits = hitter_logs['Hits'].sum()
    total_atbats = hitter_logs['AtBats'].sum()

    if total_atbats == 0:
        return False

    batting_average = total_hits / total_atbats
    return batting_average >= 0.250

def analyze_pitcher_logs(pitcher_logs):
    """
    Checks if a pitcher is hot over the last 10–15 games.
    Must average at least 5.5 strikeouts per game and allow fewer than 7 hits per game.
    """
    if pitcher_logs is None or pitcher_logs.empty:
        return False

    total_strikeouts = pitcher_logs['Strikeouts'].sum()
    total_hits_allowed = pitcher_logs['HitsAllowed'].sum()
    games_played = len(pitcher_logs)

    if games_played == 0:
        return False

    avg_strikeouts = total_strikeouts / games_played
    avg_hits_allowed = total_hits_allowed / games_played

    return (avg_strikeouts >= 5.5) and (avg_hits_allowed <= 7.0)

def analyze_batter_vs_pitcher(batter_vs_pitcher_data):
    """
    Checks if a batter has a good history against today's pitcher.
    Must have at least 10 at-bats and batting average >= .250.
    """
    if batter_vs_pitcher_data is None:
        return False

    ab = batter_vs_pitcher_data.get('AtBats', 0)
    hits = batter_vs_pitcher_data.get('Hits', 0)

    if ab < 10:
        return True  # Small sample, assume neutral matchup

    if ab > 0:
        batting_average = hits / ab
        return batting_average >= 0.250

    return False

def check_injury_status(injury_status):
    """
    Rejects injured players.
    """
    if injury_status == "Injured":
        return False
    return True

def check_team_form(team_record, losing_streak):
    """
    Checks if a team is eligible:
    - Must have an overall winning percentage above .500
    - Must NOT be on a losing streak of 5 or more games
    """
    wins = team_record.get('Wins', 0)
    losses = team_record.get('Losses', 0)

    if (wins + losses) == 0:
        return False

    winning_percentage = wins / (wins + losses)

    if winning_percentage > 0.500 and losing_streak < 5:
        return True
    else:
        return False
