from rest_framework import routers
from .api import ReservationViewSet, ActivityViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('api/reservations', ReservationViewSet, 'reservations')
router.register('api/activities', ActivityViewSet, 'activities')
router.register('api/users', UserViewSet, 'users')

urlpatterns = router.urls