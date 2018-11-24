from django.db import models
from accounts.models import UserHouse

# Create your models here.


class Camera(models.Model):
    id = models.IntegerField(primary_key=True)
    house = models.ForeignKey(UserHouse, on_delete=models.CASCADE)
    condition = models.TextField(max_length=30, default='Not Installed')
    cammodel = models.CharField(max_length=10, default='IP Camera')

    def __str__(self):
        return str(self.house) + "\'s camera " + str(self.id) + ":id"


class SensorAlarm(models.Model):
    id = models.IntegerField(primary_key=True)
    house = models.ForeignKey(UserHouse, on_delete=models.CASCADE)
    condition = models.TextField(max_length=30, default='Not Installed')
    alarmtype = models.CharField(max_length=10, default='PIR Sensors')

    def __str__(self):
        return str(self.house) + "\'s sensor " + str(self.id) + ":id"
