from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import LoginSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'current_rooms']
