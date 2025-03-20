from rest_framework import serializers
from .models import Forecast


class ForecastLocation(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast.objects.all()
        fields = [
            'id',
            'location',
            'forecast_date',
            'temperature_min',
            'temperature_max',
            'humidity',
            'precipitation_probability',
            'wind_speed',
            'wind_description',
            ''
        ]