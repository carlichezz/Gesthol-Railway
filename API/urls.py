from rest_framework import routers
from .api import ReservaViewSet,ActividadViewSet

router = routers.DefaultRouter()
router.register('api/reservas',ReservaViewSet,'reservas')
router.register('api/actividades', ActividadViewSet, 'actividades')

urlpatterns = router.urls