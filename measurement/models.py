from django.db import models


class Sensor(models.Model):
    """Модель датчика температуры"""
    name = models.CharField(max_length=50)
    description = models.TextField()


class Measurement(models.Model):
    """Модель измерения температуры с указанием id датчика-измерителя"""
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, default=None, related_name='measurements')
    picture = models.ImageField(default=None, null=True)  # добавил поле с картинкой.

