from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    """Этот сериалайзер обрабатывает датчики"""
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    """Этот сериалайзер обрабатывает измерения температуры"""
    picture = serializers.ImageField(allow_empty_file=True, allow_null=True)  # добавил поле с картинкой.

    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'created_at', 'picture']


class SensorDetailSerializer(serializers.ModelSerializer):
    """Этот сериалайзер обрабатывает датчик и все его температуры"""
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
