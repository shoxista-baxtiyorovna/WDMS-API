from django.db.models import Avg, Sum, Max
from rest_framework.response import Response
from rest_framework.decorators import api_view
from weather.models import WeatherData


@api_view(['GET'])
def average_temperature_view(request):
    avg_value = WeatherData.objects.aggregate(average_temperature=Avg('temperature'))
    return Response(avg_value)


@api_view(['GET'])
def precipitation_sum_view(request):
    value_sum = WeatherData.objects.aggregate(precipitation_sum=Sum('precipitation'))
    return Response(value_sum)


@api_view(['GET'])
def wind_speed_max_view(request):
    max_value = WeatherData.objects.aggregate(wind_speed_max=Max('wind_speed'))
    return Response(max_value)