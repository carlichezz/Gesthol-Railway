from .models import Reserva,Actividad
from rest_framework import serializers
from django.contrib.auth.models import User

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('__all__')


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','email','password','is_staff']