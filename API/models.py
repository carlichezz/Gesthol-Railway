from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    client = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_count = models.IntegerField()
    room_count = models.IntegerField()


class Activity(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    photo = models.CharField(max_length=500,default="")
    description = models.CharField(max_length=1000,default="",null=True)
