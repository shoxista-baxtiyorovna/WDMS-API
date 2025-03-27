from rest_framework import generics
from .serializers import WeatherDataSerializer, WeatherDataByLocationSerializer
from .pagination import WeatherDataPagination, WeatherDataByLocationPagination
from .models import WeatherData


class WeatherDataListCreateView(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    pagination_class = WeatherDataPagination


class WeatherDataRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer


class WeatherDataByLocationView(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataByLocationSerializer
    pagination_class = WeatherDataByLocationPagination

    def get_queryset(self):
        return super().get_queryset().filter(location__id=self.kwargs['pk'])

