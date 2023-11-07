import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model

User = get_user_model()


def update_rooms_list(user, room_name):
    rooms_list = user.get_current_rooms()

    if room_name not in rooms_list:
        rooms_list = [*rooms_list, room_name]

    user.update_current_rooms(rooms_list)
    user.save()


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']["room_name"]
        self.room_group_name = f'chat_{self.room_name}'
        username1, username2 = self.room_name.split("_")

        user1 = User.objects.get(username=username1)
        user2 = User.objects.get(username=username2)
        print(self.scope['user'])

        update_rooms_list(user1, self.room_name)
        update_rooms_list(user2, self.room_name)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Recieve message from websocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Recieve message from group
    def chat_message(self, event):
        message = event["message"]

        # Send message to websocket
        self.send(text_data=json.dumps(message))
