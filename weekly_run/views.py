from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Weeklymain, Weeklysub


class WeeklyView(generic.ListView):
    template_name = 'weekly_run/weekly.html'
    context_object_name = 'latest_weekly_list'

    def get_queryset(self):
        return Weeklymain.objects.order_by('-slip_date')[:5]


class WeekdetView(generic.DetailView):
    model = Weeklysub
    template_name = 'weekly_run/weekdet.html'
