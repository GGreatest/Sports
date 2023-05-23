
import requests
import datetime
import json


def get_fixture_data():
    # Az aktuális dátum lekérése
    today = datetime.date.today()

    # Az adat létrehozása
    data = {"date": str(today)}

    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    headers = {
        "X-RapidAPI-Key": "83a8465b14msh129c345fb9ff431p1933f1jsn5fecb2390cf0",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=data)
    fixtures = response.json()['response']

    for fixture in fixtures:
        league_id = fixture['league']['id']
        if league_id in [39, 2, 61, 78, 135]:
            country = fixture['league']['country']
            date = fixture['fixture']['date']
            match_id = fixture['fixture']['id']
            flag = fixture['league']['flag']
            league = fixture['league']['name']
            home_team = fixture['teams']['home']['name']
            away_team = fixture['teams']['away']['name']
            home_team_logo = fixture['teams']['home']['logo']
            away_team_logo = fixture['teams']['away']['logo']
            print(date, country, league, home_team, "vs", away_team, match_id)

            get_predictions(match_id)

def get_predictions(match_id):
    url = "https://api-football-v1.p.rapidapi.com/v3/predictions"
    headers = {
        "X-RapidAPI-Key": "83a8465b14msh129c345fb9ff431p1933f1jsn5fecb2390cf0",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    params = {"fixture": match_id}

    response = requests.get(url, headers=headers, params=params)
    predictions = response.json()['response']

    prediction = predictions[0]
    winner_team_name = prediction['predictions']['winner']['name']
    home_percent = prediction['predictions']['percent']['home']
    draw_percent = prediction['predictions']['percent']['draw']
    away_percent = prediction['predictions']['percent']['away']
    advice = prediction['predictions']['advice']
    # home last five matches
    home_form = prediction['teams']['home']['last_5']['form']
    home_attack = prediction['teams']['home']['last_5']['att']
    home_def = prediction['teams']['home']['last_5']['def']
    home_goals_total = prediction['teams']['home']['last_5']['goals']['for']['total']
    home_goals_average = prediction['teams']['home']['last_5']['goals']['for']['average']
    home_goals_against_total = prediction['teams']['home']['last_5']['goals']['against']['total']
    home_goals_against_average = prediction['teams']['home']['last_5']['goals']['against']['average']
    # away last five matches
    away_form = prediction['teams']['away']['last_5']['form']
    away_attack = prediction['teams']['away']['last_5']['att']
    away_def = prediction['teams']['away']['last_5']['def']
    away_goals_total = prediction['teams']['away']['last_5']['goals']['for']['total']
    away_goals_average = prediction['teams']['away']['last_5']['goals']['for']['average']
    away_goals_against_total = prediction['teams']['away']['last_5']['goals']['against']['total']
    away_goals_against_average = prediction['teams']['away']['last_5']['goals']['against']['average']

    print(home_form, home_attack, home_def, home_goals_total, home_goals_average, away_goals_total,
          away_goals_average, home_goals_against_total)

def get_daily_betting_tips():
    url = "https://daily-betting-tips.p.rapidapi.com/daily-betting-tip-api/items/daily_betting_tips"
    headers = {
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "X-RapidAPI-Key": "83a8465b14msh129c345fb9ff431p1933f1jsn5fecb2390cf0",
        "X-RapidAPI-Host": "daily-betting-tips.p.rapidapi.com"
    }
    today = datetime.date.today()

    params = {"q": today.strftime("%d.%m.%Y"), "sort": "-id"}

    response = requests.get(url, headers=headers, params=params)
    predictions = response.json()['data']

    for match in predictions:
        league_name = match['league_name']
        home_team = match['home_team']
        away_team = match['away_team']
        odd_value = match['odd_value']
        game_prediction = match['game_prediction']
        match_date = match['match_date']
        match_time = match['match_time']
        sport_type = match['sport_type']

        print("Bajnokság:", league_name)
        print("Hazai csapat:", home_team)
        print("Vendégcsapat:", away_team)
        print("Odds érték:", odd_value)
        print("Játék előrejelzése:", game_prediction)
        print("Meccs dátuma:", match_date)
        print("Meccs időpontja:", match_time)
        print("Sporttípus:", sport_type)

get_fixture_data()
get_daily_betting_tips()
