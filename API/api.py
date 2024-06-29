from rest_framework import viewsets, permissions
from .models import Reserva,Actividad
from .serializers import ReservaSerializer,ActividadSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes
from django.contrib.auth.models import User

@authentication_classes([TokenAuthentication])
class ReservaViewSet (viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    permission_classes = [IsAuthenticated] #PROVICIONAL
    serializer_class = ReservaSerializer

@authentication_classes([TokenAuthentication])
class ActividadViewSet (viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly] #PROVICIONAL
    serializer_class = ActividadSerializer

@authentication_classes([TokenAuthentication])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
