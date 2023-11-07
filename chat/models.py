import json
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=50, null=True, blank=True)
    current_rooms = models.CharField(max_length=1000, default="[]")
    REQUIRED_FIELDS = []

    def update_current_rooms(self, room_names):
        self.current_rooms = json.dumps(room_names)

    def get_current_rooms(self):
        return json.loads(self.current_rooms)


class Chat(models.Model):
    message = models.CharField(
        max_length=300, default="", null=False, blank=False)
    sender_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=False, related_name="sender")
    reciever_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=False, related_name="reciever")
    time_sent = models.DateTimeField()
    time_recieved = models.DateTimeField()
    seen = models.BooleanField(default=False)
