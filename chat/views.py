import json
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics

from . import serializers

User = get_user_model()


class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    Permission_class = [AllowAny]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.UserSerializer(queryset, many=True)

        for data in serializer.data:
            data['current_rooms'] = json.loads(data['current_rooms'])
        return Response(serializer.data)
