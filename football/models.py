from django.db import models


class FixtureData(models.Model):
    league_id = models.IntegerField()
    country = models.CharField(max_length=255)
    date = models.DateTimeField()
    match_id = models.IntegerField()
    flag = models.CharField(max_length=255)
    league = models.CharField(max_length=255)
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    home_team_logo = models.URLField()
    away_team_logo = models.URLField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"


class PredictionData(models.Model):
    match_id = models.IntegerField()
    winner_team_name = models.CharField(max_length=255)
    home_percent = models.FloatField()
    draw_percent = models.FloatField()
    away_percent = models.FloatField()
    advice = models.CharField(max_length=255)
    home_form = models.CharField(max_length=255)
    home_attack = models.CharField(max_length=255)
    home_def = models.CharField(max_length=255)
    home_goals_total = models.IntegerField()
    home_goals_average = models.FloatField()
    home_goals_against_total = models.IntegerField()
    home_goals_against_average = models.FloatField()
    away_form = models.CharField(max_length=255)
    away_attack = models.CharField(max_length=255)
    away_def = models.CharField(max_length=255)
    away_goals_total = models.IntegerField()
    away_goals_average = models.FloatField()
    away_goals_against_total = models.IntegerField()
    away_goals_against_average = models.FloatField()

    def __str__(self):
        return f"Prediction for match ID: {self.match_id}"


class BettingTipData(models.Model):
    league_name = models.CharField(max_length=255)
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    odd_value = models.FloatField()
    game_prediction = models.CharField(max_length=255)
    match_date = models.DateField()
    match_time = models.TimeField()
    sport_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"
