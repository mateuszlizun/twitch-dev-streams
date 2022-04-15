import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class StreamsConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "streams"
        self.room_group_name = "streams_group"

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

    def streams_list(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"type": "streams", "message": message}))
