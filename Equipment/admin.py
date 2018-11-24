from django.contrib import admin

from.models import Camera, SensorAlarm

# Register your models here.

admin.site.register(Camera)
admin.site.register(SensorAlarm)