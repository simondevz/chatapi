from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers

User = get_user_model()
# Create your views here.


def index(request):
    return HttpResponse('hi there')


class ListAvailableUsers(APIView):
    def get(self, request):
        data = serializers.ListUserSerialisers(User.objects.all(), many=True)
        return Response(data.data, headers={'Access-Control-Allow-Origin': '*'
                                            })
