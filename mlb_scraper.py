# mlb_scraper.py

import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0'
}

# ===============================
# Lineup Scrapers
# ===============================

def scrape_today_lineups_espn():
    url = "https://www.espn.com/mlb/lineups"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    players = []
    lineup_sections = soup.find_all('section', class_='Lineup__Table')

    for section in lineup_sections:
        names = section.find_all('a', class_='AnchorLink')
        for name_tag in names:
            name = name_tag.text.strip()
            players.append({'player_name': name})

    return players

def scrape_today_lineups_yahoo():
    url = "https://sports.yahoo.com/mlb/players/"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    players = []
    names = soup.find_all('a', class_='Fz(xs) Ell C($c-fuji-blue-1-b)')

    for name_tag in names:
        name = name_tag.text.strip()
        players.append({'player_name': name})

    return players

def scrape_today_lineups_mlb():
    url = "https://www.mlb.com/starting-lineups"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    players = []
    names = soup.find_all('span', class_='starting-lineup__player-name')

    for name_tag in names:
        name = name_tag.text.strip()
        players.append({'player_name': name})

    return players

def scrape_today_lineups_fangraphs():
    url = "https://www.fangraphs.com/roster-resource/depth-charts"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    players = []
    names = soup.find_all('td', class_='depth_chart-player-name')

    for name_tag in names:
        name = name_tag.text.strip()
        players.append({'player_name': name})

    return players

def scrape_today_lineups_baseballreference():
    url = "https://www.baseball-reference.com/leagues/MLB/2024-standard-batting.shtml"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    players = []
    names = soup.find_all('td', {'data-stat': 'player'})

    for name_tag in names:
        name = name_tag.text.strip()
        players.append({'player_name': name})

    return players

# ===============================
# BVP Scrapers (Placeholder for future upgrade)
# ===============================

def scrape_bvp_espn(batter_name, pitcher_name):
    return {}

def scrape_bvp_yahoo(batter_name, pitcher_name):
    return {}

def scrape_bvp_mlb(batter_name, pitcher_name):
    return {}

def scrape_bvp_fangraphs(batter_name, pitcher_name):
    return {}

def scrape_bvp_baseballreference(batter_name, pitcher_name):
    return {}





