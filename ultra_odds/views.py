from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Ultramain, Ultrasub


class UltraView(generic.ListView):
    template_name = 'ultra_odds/ultra.html'
    context_object_name = 'latest_ultra_list'

    def get_queryset(self):
        return Ultramain.objects.order_by('-slip_date')[:5]


class UltradetView(generic.DetailView):
    model = Ultrasub
    template_name = 'ultra_odds/ultradet.html'
