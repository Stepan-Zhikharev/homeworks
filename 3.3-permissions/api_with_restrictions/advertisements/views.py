from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement

from advertisements.serializers import AdvertisementSerializer


from advertisements.permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update"]:
    #         return [IsAuthenticated()]
    #     return []
