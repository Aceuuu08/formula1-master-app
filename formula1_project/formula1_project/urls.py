"""
URL configuration for formula1_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from formula1_app.views import Home, TeamListView, DriverListView, RaceListView, ResultListView, ChampionshipListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('team_list/', TeamListView.as_view(), name='team-list'),
    path('driver_list/', DriverListView.as_view(), name='driver-list'),
    path('race_list/', RaceListView.as_view(), name='race-list'),
    path('result_list/', ResultListView.as_view(), name='result-list'),
    path('championship_list/', ChampionshipListView.as_view(), name='championship-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 