# ballpark_factors.py

def get_ballpark_factor(team_home_city):
    """
    Returns the ballpark type for the team's home stadium.

    Args:
        team_home_city (str): City where the game is played.

    Returns:
        str: 'Hitter', 'Pitcher', or 'Neutral'
    """

    hitter_friendly_parks = [
        'Denver',       # Coors Field (Rockies)
        'Boston',       # Fenway Park (Red Sox)
        'Cincinnati',   # Great American Ballpark (Reds)
        'Philadelphia', # Citizens Bank Park (Phillies)
        'Chicago',      # Wrigley Field (Cubs, when wind blowing out)
        'Baltimore',    # Camden Yards (Orioles)
    ]

    pitcher_friendly_parks = [
        'Oakland',      # Oakland Coliseum (Athletics)
        'Miami',        # LoanDepot Park (Marlins)
        'Seattle',      # T-Mobile Park (Mariners)
        'San Francisco',# Oracle Park (Giants)
        'San Diego',    # Petco Park (Padres)
        'Detroit',      # Comerica Park (Tigers)
        'New York',     # Citi Field (Mets) - NOT Yankees
    ]

    # Normalize city name (sometimes ESPN might give team name instead of city)
    city_normalized = team_home_city.lower()

    for city in hitter_friendly_parks:
        if city.lower() in city_normalized:
            return 'Hitter'

    for city in pitcher_friendly_parks:
        if city.lower() in city_normalized:
            return 'Pitcher'

    return 'Neutral'
