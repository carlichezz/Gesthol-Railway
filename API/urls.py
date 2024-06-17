from rest_framework import routers
from .api import ReservaViewSet,ActividadViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('api/reservas',ReservaViewSet,'reservas')
router.register('api/actividades', ActividadViewSet, 'actividades')
router.register('api/users', UserViewSet, 'users')
urlpatterns = router.urls