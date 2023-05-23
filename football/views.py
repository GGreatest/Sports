from django.shortcuts import render
from django.shortcuts import render
from models import FixtureData, PredictionData, BettingTipData
from serializers import FixtureDataSerializer, PredictionDataSerializer, BettingTipDataSerializer
import requests
import datetime


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
            serializer = FixtureDataSerializer(data=fixture)
            if serializer.is_valid():
                serializer.save()
            else:
                print('FixtureData Serializer is not valid:', serializer.errors)


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
    serializer = PredictionDataSerializer(data=prediction)
    if serializer.is_valid():
        serializer.save()
    else:
        print('PredictionData Serializer is not valid:', serializer.errors)


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
    betting_tips = response.json()['data']

    for match in betting_tips:
        serializer = BettingTipDataSerializer(data=match)
        if serializer.is_valid():
            serializer.save()
        else:
            print('BettingTipData Serializer is not valid:', serializer.errors)


def update_data(request):
    get_fixture_data()
    # Call get_predictions() for each fixture ID
    fixtures = FixtureData.objects.all()
    for fixture in fixtures:
        get_predictions(fixture.match_id)
    
    get_daily_betting_tips()

    return render(request, 'your_template.html')

