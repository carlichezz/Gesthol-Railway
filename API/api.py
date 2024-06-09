from rest_framework import viewsets, permissions
from .models import Reserva,Actividad
from .serializers import ReservaSerializer,ActividadSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes

@authentication_classes([TokenAuthentication])
class ReservaViewSet (viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    permission_classes = [IsAuthenticated] #PROVICIONAL
    serializer_class = ReservaSerializer

@authentication_classes([TokenAuthentication])
class ActividadViewSet (viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    permission_classes = [IsAuthenticated] #PROVICIONAL
    serializer_class = ActividadSerializer