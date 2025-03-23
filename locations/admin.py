from django.contrib import admin
from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'latitude', 'longitude', 'elevation', 'created_at']
    search_field = ['name']


