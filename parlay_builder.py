from collections import defaultdict

def group_players_by_game(eligible_players):
    """
    Groups players by their game matchup.

    Args:
        eligible_players (list of dict): 
            Example: [{'name': 'Vlad Jr.', 'team': 'Blue Jays', 'opponent': 'Yankees'}, ...]

    Returns:
        dict: key = (team, opponent), value = list of players
    """
    grouped = defaultdict(list)

    for player in eligible_players:
        matchup_key = (player['team'], player['opponent'])
        grouped[matchup_key].append(player)

    return grouped

def build_same_game_parlays(grouped_players):
    """
    Builds same game parlays based on players grouped by game.

    Args:
        grouped_players (dict): Output from group_players_by_game()

    Returns:
        list: parlays (2-leg, 3-leg, or VIP single picks)
    """
    parlays = []

    for matchup, players in grouped_players.items():
        if len(players) >= 3:
            parlays.append({
                'type': '3-Leg SGP',
                'matchup': matchup,
                'players': [p['name'] for p in players[:3]]
            })
        elif len(players) == 2:
            parlays.append({
                'type': '2-Leg SGP',
                'matchup': matchup,
                'players': [p['name'] for p in players]
            })
        elif len(players) == 1:
            parlays.append({
                'type': 'VIP Single Prop',
                'matchup': matchup,
                'players': [players[0]['name']]
            })

    return parlays

