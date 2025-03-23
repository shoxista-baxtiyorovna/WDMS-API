from django.contrib import admin
from .models import Forecast


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'forecast_date']
    search_fields = ['location']