from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from daily_odds.models import DailySub, DailyMain
from ultra_odds.models import Ultrasub, Ultramain
from weekly_run.models import Weeklysub, Weeklymain
from datetime import date, datetime


class PrevDailyView(generic.ListView):
    template_name = 'history/prev_daily.html'
    context_object_name = 'latest_prev_daily_list'

    def get_queryset(self):
        return DailyMain.objects.order_by('-slip_date')[:5]


class PrevUltraView(generic.ListView):
    template_name = 'history/prev_ultra.html'
    context_object_name = 'latest_prev_ultra_list'

    def get_queryset(self):
        return Ultramain.objects.order_by('-slip_date')[:5]


class PrevWeeklyView(generic.ListView):
    template_name = 'history/prev_weekly.html'
    context_object_name = 'latest_prev_weekly_list'

    def get_queryset(self):
        return Weeklymain.objects.order_by('-slip_date')[:5]
