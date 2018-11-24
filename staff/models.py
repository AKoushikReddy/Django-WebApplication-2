from django.db import models
from accounts.models import UserHouse

# Create your models here.


class Staff(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    salary = models.IntegerField()
    remark = models.TextField(max_length=25)

    def __str__(self):
        return str(self.name)


class HeadStaff(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    house = models.OneToOneField(UserHouse, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.staff)
