from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import DailyMain, DailySub


class IndexView(generic.ListView):
    template_name = 'daily_odds/index.html'
    context_object_name = 'latest_daily_list'

    def get_queryset(self):
        return DailyMain.objects.order_by('-slip_date')[:5]


class DailydetView(generic.DetailView):
    model = DailySub
    template_name = 'daily_odds/dailydet.html'
