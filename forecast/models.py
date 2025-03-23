from django.db import models
from locations.models import Location


class Forecast(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='forecast')
    forecast_date = models.DateField()
    temperature_min = models.FloatField()
    temperature_max = models.FloatField()
    humidity = models.FloatField()
    precipitation_probability = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

