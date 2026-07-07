from rest_framework import viewsets, permissions
from .models import Reservation, Activity
from .serializers import ReservationSerializer, ActivitySerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes
from django.contrib.auth.models import User

@authentication_classes([TokenAuthentication])
class ReservationViewSet (viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    permission_classes = [IsAuthenticated] #TEMPORARY
    serializer_class = ReservationSerializer

@authentication_classes([TokenAuthentication])
class ActivityViewSet (viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly] #TEMPORARY
    serializer_class = ActivitySerializer

@authentication_classes([TokenAuthentication])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
