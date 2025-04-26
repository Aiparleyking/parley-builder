# cross_check.py

def cross_check_lineups(scrapes):
    """
    Takes a list of all site scrapes and returns confirmed starters.

    Args:
        scrapes (list): List of lists of player names from different sites.

    Returns:
        list: Confirmed player names (seen in at least 2 sources).
    """
    player_count = {}

    for scrape in scrapes:
        for player in scrape:
            name = player['player_name']
            player_count[name] = player_count.get(name, 0) + 1

    confirmed_players = [name for name, count in player_count.items() if count >= 2]

    return confirmed_players


def cross_check_bvp_histories(bvp_scrapes):
    """
    Takes a list of all BVP scrapes and returns merged BVP stats.

    Args:
        bvp_scrapes (list): List of dictionaries { 'batter_name': {'at_bats': x, 'hits': y} }

    Returns:
        dict: Merged BVP info for confirmed hitters.
    """

    merged_bvp = {}

    for scrape in bvp_scrapes:
        for batter, stats in scrape.items():
            if batter not in merged_bvp:
                merged_bvp[batter] = {'at_bats': 0, 'hits': 0}
            merged_bvp[batter]['at_bats'] += stats.get('at_bats', 0)
            merged_bvp[batter]['hits'] += stats.get('hits', 0)

    return merged_bvp

