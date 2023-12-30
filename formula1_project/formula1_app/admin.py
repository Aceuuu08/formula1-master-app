from django.contrib import admin
from .models import Driver, Team, Race, Result

class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at')

class DriverAdmin(BaseModelAdmin):
    list_display = ('name', 'nationality', 'birth_date', 'team', 'created_at', 'updated_at')

class TeamAdmin(BaseModelAdmin):
    list_display = ('name', 'country', 'team_principal', 'created_at', 'updated_at')

class RaceAdmin(BaseModelAdmin):
    list_display = ('title', 'date', 'location', 'created_at', 'updated_at')

class ResultAdmin(BaseModelAdmin):
    list_display = ('race', 'driver', 'position', 'best_lap_time', 'created_at', 'updated_at')

# Register the models with their respective Admin classes
admin.site.register(Driver, DriverAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Result, ResultAdmin)