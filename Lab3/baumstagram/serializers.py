from baumstagram.models import *
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Accounts
        # Поля, которые мы сериализуем
        fields = ["idaccounts", "iduser", "idphoto", "followerscount"]

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Photos
        # Поля, которые мы сериализуем
        fields = ["idphoto", "title", "path", "date", "description"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Users
        # Поля, которые мы сериализуем
        fields = ["iduser", "name", "surname", "email"]