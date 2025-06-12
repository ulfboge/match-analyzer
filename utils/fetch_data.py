import requests
import time
import os

API_KEY = os.getenv("RAPIDAPI_KEY") or "DIN_API_NYCKEL"
BASE_URL = "https://api-football-v1.p.rapidapi.com/v3"
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}


def search_team_id(team_name):
    url = f"{BASE_URL}/teams"
    querystring = {"search": team_name}
    response = requests.get(url, headers=HEADERS, params=querystring)
    if response.status_code == 200:
        data = response.json()
        if data['response']:
            return data['response'][0]['team']['id']
    return None


def get_form(team_id):
    url = f"{BASE_URL}/teams/statistics"
    params = {"team": team_id, "season": 2023, "league": 39}  # Exempel: Premier League (id=39)
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code != 200:
        return "Okänd"

    matches = response.json().get("form", "")
    return ", ".join(matches)


def get_table_position(team_id):
    url = f"{BASE_URL}/standings"
    params = {"season": 2023, "league": 39}  # Premier League
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code != 200:
        return "Okänd"
    table = response.json()["response"][0]["league"]["standings"][0]
    for team in table:
        if team["team"]["id"] == team_id:
            pos = team["rank"]
            return f"{team['team']['name']}: {pos}:e plats"
    return "Okänd"


def get_match_stats(match_list):
    results = []
    for match in match_list:
        try:
            home, away = [t.strip() for t in match.split("-")]
            home_id = search_team_id(home)
            away_id = search_team_id(away)

            home_form = get_form(home_id) if home_id else "Okänd"
            away_form = get_form(away_id) if away_id else "Okänd"

            table_info = f"{get_table_position(home_id)}, {get_table_position(away_id)}"

            result = {
                "teams": f"{home} vs {away}",
                "home_form": home_form,
                "away_form": away_form,
                "table": table_info,
                "injuries": f"Ingen skadeinformation tillgänglig via API-Football för {home} och {away}."
            }
            results.append(result)
            time.sleep(1)
        except Exception as e:
            results.append({
                "teams": match,
                "home_form": "Fel",
                "away_form": "Fel",
                "table": "Fel",
                "injuries": "Fel vid hämtning"
            })
    return results