from django.db import models
import datetime

from django.db import models
from django.utils import timezone


class DailyMain(models.Model):
    slip_date = models.DateTimeField('slip_date', default=None)
    slip_name = models.CharField(max_length=40, null=True, blank=True)

    def name(self):
        return self.outcome

    def recent_slips(self):
        now = timezone.now()
        return now - datetime.timedelta(days=40) <= self.slip_date <= now

    def showing_prev(self):
        now = timezone.now()
        yester = now - datetime.timedelta(1)
        return now - datetime.timedelta(days=40) <= self.slip_date <= yester





class DailySub(models.Model):
    daily_main = models.ForeignKey(DailyMain, on_delete=models.CASCADE, default=None)
    country = models.CharField(max_length=30, default=None)
    home_team = models.CharField(max_length=30)
    away_team = models.CharField(max_length=30)
    prediction = models.CharField(max_length=40)
    outcome = models.CharField(max_length=20, null=True, blank=True)
    match_date = models.DateTimeField('match date')
    h2h_home = models.CharField(max_length=30, default=None)
    h2h_away = models.CharField(max_length=30, default=None)
    h2h_draw = models.CharField(max_length=30, default=None)
    standings_home = models.CharField(max_length=30, default=None)
    standings_away = models.CharField(max_length=30, default=None)
    form_home = models.CharField(max_length=30, default=None)
    form_away = models.CharField(max_length=30, default=None)
    goals_home = models.IntegerField(default=None)
    goals_away = models.IntegerField(default=None)
    missing_players_home = models.CharField(max_length=300, default=None)
    missing_players_away = models.CharField(max_length=300, default=None)

    def __str__(self):
        return self.home_team

    def __str__(self):
        return self.away_team

    def __str__(self):
        return self.prediction

    def match_outcome(self):
        return self.outcome

    def recent_matches(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.match_date <= now
