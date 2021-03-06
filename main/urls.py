from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_address', views.get_address, name='get_address'),
    path('journeytime', views.journeytime, name='journeytime'),
    path('lines', views.lines, name='lines'),
    path('locations', views.locations, name='locations'),
    path('stops', views.stops, name='stops'),
    path('get_switch', views.get_switch, name='get_switch'),
    path('get_timetable',views.get_timetable,name='get_timetable'),
    path('get_fares', views.get_fares, name='get_fares')

]
