from django.urls import path
from . import views

urlpatterns = [
    path('analytics/temperature-avg/', views.average_temperature_view, name='temperature-avg'),
    path('analytics/precipitation-sum/', views.precipitation_sum_view, name='precipitation-sum'),
    path('analytics/wind-speed-max/', views.wind_speed_max_view, name='wind-speed-max'),
]