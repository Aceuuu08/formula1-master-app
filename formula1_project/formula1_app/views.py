from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Team, Driver, Race, Result, Championship

class Home(ListView):
    model = Driver
    content_onject_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
# TEAM    
class TeamListView(ListView):
    model = Team
    context_object_name = 'teams'
    template_name = 'team_list.html'
    paginate_by = 4

# DRIVER
class DriverListView(ListView):
    model = Driver
    context_object_name = 'drivers'
    template_name = 'driver_list.html'
    paginate_by = 4

# RACE
class RaceListView(ListView):
    model = Race
    context_object_name = 'races'
    template_name = 'race_list.html'
    paginate_by = 7

# RESULT
class ResultListView(ListView):
    model = Result
    context_object_name = 'results'
    template_name = 'result_list.html'
    paginate_by = 5

# CHAMPIONSHIP
class ChampionshipListView(ListView):
    model = Championship
    context_object_name = 'championships'
    template_name = 'championship_list.html'
    paginate_by = 5
