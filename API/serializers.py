from .models import Reserva,Actividad
from rest_framework import serializers


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('__all__')


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ('__all__')