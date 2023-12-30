from django.shortcuts import render
from django.views import View
from .models import Team, Driver, Race, Result, Championship

class TeamListView(View):
    def get(self, request):
        teams = Team.objects.all()
        return render(request, 'team_list.html', {'teams': teams})

class DriverListView(View):
    def get(self, request):
        drivers = Driver.objects.all()
        return render(request, 'driver_list.html', {'drivers': drivers})

class RaceListView(View):
    def get(self, request):
        races = Race.objects.all()
        return render(request, 'race_list.html', {'races': races})

class ResultListView(View):
    def get(self, request):
        results = Result.objects.all()
        return render(request, 'result_list.html', {'results': results})
    
class ChampionshipListView(View):
    def get(self, request):
        championships = Championship.objects.all()
        return render(request, 'championship_list.html', {'championships': championships})
