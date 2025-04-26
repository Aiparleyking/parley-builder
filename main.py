# main.py

from mlb_scraper import (
    scrape_today_lineups_espn,
    scrape_today_lineups_yahoo,
    scrape_today_lineups_mlb,
    scrape_today_lineups_fangraphs,
    scrape_today_lineups_baseballreference
)

from player_filters import (
    analyze_hitter_logs,
    analyze_pitcher_logs,
    analyze_batter_vs_pitcher,
    check_injury_status,
    check_team_form
)

from parlay_builder import (
    group_players_by_game,
    build_same_game_parlays
)

from cross_check import (
    cross_check_lineups
)

from vip_system import is_vip_pick
from confidence_rater import rate_confidence
from auto_save import save_daily_picks
from weather_scraper import get_weather_forecast
from ballpark_factors import get_ballpark_factor

import time

def main():
    print("Scraping today's MLB lineups from multiple sources...")

    # Scrape all sources
    espn_lineups = scrape_today_lineups_espn()
    yahoo_lineups = scrape_today_lineups_yahoo()
    mlb_lineups = scrape_today_lineups_mlb()
    fangraphs_lineups = scrape_today_lineups_fangraphs()
    bbr_lineups = scrape_today_lineups_baseballreference()

    all_scrapes = [espn_lineups, yahoo_lineups, mlb_lineups, fangraphs_lineups, bbr_lineups]

    # Cross-validate starters
    confirmed_players = cross_check_lineups(all_scrapes)

    if not confirmed_players:
        print("⚠️ No confirmed starting players found. Try again closer to game time.")
        return [], []  # <- RETURN EMPTY PICKS

    print(f"\n✅ Confirmed {len(confirmed_players)} starters after cross-validation.")

    eligible_players = []
    vip_players = []

    for player_name in confirmed_players:
        print(f"\nAnalyzing {player_name}...")

        passed_core = True  # Assume basic pass for now
        
        team_name = "FakeTeam"
        opponent_name = "FakeOpponent"

        weather = {'WindSpeed': 10, 'WindDirection': 'W'}
        weather_boost = "Neutral"
        if weather:
            if weather['WindSpeed'] >= 8:
                if weather['WindDirection'] in ['W', 'SW', 'NW']:
                    weather_boost = "Good"
                else:
                    weather_boost = "Bad"

        ballpark_type = 'Neutral'
        ballpark_boost = "Neutral"
        if ballpark_type == 'Hitter':
            ballpark_boost = "Good"
        elif ballpark_type == 'Pitcher':
            ballpark_boost = "Bad"

        player_data = {
            'name': player_name,
            'team': team_name,
            'opponent': opponent_name,
            'CorePassed': passed_core,
            'WeatherBoost': weather_boost,
            'BallparkBoost': ballpark_boost
        }

        if is_vip_pick(player_data):
            player_data['VIP'] = True
            vip_players.append({
                'name': player_name,
                'team': team_name,
                'opponent': opponent_name,
                'confidence': rate_confidence(player_data)
            })
        else:
            player_data['VIP'] = False
            eligible_players.append({
                'name': player_name,
                'team': team_name,
                'opponent': opponent_name,
                'confidence': rate_confidence(player_data)
            })

        print(f"✅ {player_name} PASSED filters! VIP: {player_data['VIP']} Confidence: {rate_confidence(player_data)} Stars")

        time.sleep(0.5)

    # Save picks
    save_daily_picks(eligible_players, vip_players)

    return eligible_players, vip_players  # <- RETURN PICKS to Streamlit

