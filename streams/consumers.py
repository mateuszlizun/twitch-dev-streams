import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class CurrentDateConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "current_date"
        self.room_group_name = "current_date_group"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

    def date_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"type": "current_date", "message": message}))
