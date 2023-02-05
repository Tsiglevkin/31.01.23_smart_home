
from rest_framework import generics
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class CreateSensorView(generics.ListCreateAPIView):
    """Класс позволяет добавить датчик и получить список всех датчиков"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorChange(generics.RetrieveUpdateAPIView):
    """Класс позволяет получить данные конкретного датчика с температурами"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurmentCreate(generics.ListCreateAPIView):
    """Класс позволяет добавить измерение и получить список всех измерений"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


