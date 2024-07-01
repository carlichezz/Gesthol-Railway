from django.db import models
from django.contrib.auth.models import User

class Reserva(models.Model):
    cliente = models.CharField(max_length=100)
    tipohabitacion = models.CharField(max_length=100)
    checkin = models.DateField()
    checkout = models.DateField()
    cantp = models.IntegerField()
    canth = models.IntegerField()


class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    fecha_y_hora = models.DateTimeField()
    foto = models.CharField(max_length=500,default="")
    descripcion = models.CharField(max_length=1000,default="",null=True)
