from django.db import models
from django.contrib.auth.models import User

class Reserva(models.Model):
    cliente = models.ForeignKey(User,on_delete=models.CASCADE)
    tipohabitacion = models.CharField(max_length=100)
    checkin = models.DateField()
    checkout = models.DateField()
    cantp = models.IntegerField()
    canth = models.IntegerField()


class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    fecha_y_hora = models.DateTimeField()
