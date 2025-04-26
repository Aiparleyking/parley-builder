import requests
from bs4 import BeautifulSoup

def get_weather_forecast(team_home_city):
    """
    Scrapes basic weather for the MLB team's city from weather.com.

    Args:
        team_home_city (str): Name of the city.

    Returns:
        dict: {'WindDirection': str, 'WindSpeed': int}
    """
    city_to_weather_url = {
        'New York': 'https://weather.com/weather/today/l/USNY0996:1:US',         # Yankees, Mets
        'Toronto': 'https://weather.com/weather/today/l/CAXX0504:1:CA',           # Blue Jays
        'Boston': 'https://weather.com/weather/today/l/USMA0046:1:US',            # Red Sox
        'Los Angeles': 'https://weather.com/weather/today/l/USCA0638:1:US',       # Dodgers, Angels
        'Philadelphia': 'https://weather.com/weather/today/l/USPA1276:1:US',      # Phillies
        'Houston': 'https://weather.com/weather/today/l/USTX0617:1:US',           # Astros
        'Atlanta': 'https://weather.com/weather/today/l/USGA0028:1:US',           # Braves
        'Chicago': 'https://weather.com/weather/today/l/USIL0225:1:US',           # Cubs, White Sox
        'Tampa': 'https://weather.com/weather/today/l/USFL0512:1:US',             # Rays
        'Arlington': 'https://weather.com/weather/today/l/USTX0039:1:US',         # Rangers
        'Milwaukee': 'https://weather.com/weather/today/l/USWI0411:1:US',         # Brewers
        'Minneapolis': 'https://weather.com/weather/today/l/USMN0503:1:US',       # Twins
        'St. Louis': 'https://weather.com/weather/today/l/USMO0695:1:US',         # Cardinals
        'San Diego': 'https://weather.com/weather/today/l/USCA0982:1:US',         # Padres
        'Seattle': 'https://weather.com/weather/today/l/USWA0395:1:US',           # Mariners
        'Baltimore': 'https://weather.com/weather/today/l/USMD0018:1:US',         # Orioles
        'Phoenix': 'https://weather.com/weather/today/l/USAZ0166:1:US',           # Diamondbacks
        'Cleveland': 'https://weather.com/weather/today/l/USOH0195:1:US',         # Guardians
        'Detroit': 'https://weather.com/weather/today/l/USMI0229:1:US',           # Tigers
        'Denver': 'https://weather.com/weather/today/l/USCO0105:1:US',            # Rockies
        'Oakland': 'https://weather.com/weather/today/l/USCA0794:1:US',           # Athletics
        'Miami': 'https://weather.com/weather/today/l/USFL0316:1:US',             # Marlins
        'Washington': 'https://weather.com/weather/today/l/USDC0001:1:US',        # Nationals
        'Kansas City': 'https://weather.com/weather/today/l/USMO0460:1:US',       # Royals
        'Pittsburgh': 'https://weather.com/weather/today/l/USPA1290:1:US',        # Pirates
        'Cincinnati': 'https://weather.com/weather/today/l/USOH0188:1:US',        # Reds
        'Anaheim': 'https://weather.com/weather/today/l/USCA0027:1:US',           # Angels (alternate for LA)
    }

    url = city_to_weather_url.get(team_home_city)
    if not url:
        return None  # No mapping found yet

    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        wind_section = soup.find('span', class_='Wind--windWrapper--3aqXJ undefined')
        if not wind_section:
            return None

        wind_text = wind_section.text.strip()  # Example: "SSW 10 mph"
        wind_parts = wind_text.split()

        if len(wind_parts) >= 2:
            wind_dir = wind_parts[0]
            wind_speed = int(wind_parts[1])

            return {'WindDirection': wind_dir, 'WindSpeed': wind_speed}

    except Exception as e:
        print(f"Weather scraping error: {e}")
        return None

    return None
