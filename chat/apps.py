from django.apps import AppConfig
from channels_presence.apps import RoomsConfig


class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'


class CustomRoomsConfig(RoomsConfig):
    name = 'channels_presence'
