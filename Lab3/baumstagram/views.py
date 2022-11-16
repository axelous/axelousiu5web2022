from rest_framework import viewsets
from baumstagram.serializers import *
from baumstagram.models import *

class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать аккаунты
    """
    # queryset всех аккаунтов
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer  # Сериализатор для модели

class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать фото
    """
    # queryset всех фото для фильтрации по дате последнего изменения
    queryset = Photos.objects.all().order_by('date')
    serializer_class = PhotoSerializer  # Сериализатор для модели

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать пользователя
    """
    # queryset всех пользователей для фильтрации по никнейму
    queryset = Users.objects.all().order_by('name')
    serializer_class = UserSerializer  # Сериализатор для модели