from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from decouple import config
from django.core.cache import cache
import requests

from .utils import set_stream_properties
from .models import Tag


@shared_task
def get_streams():
    r_streams = requests.get(
        "https://api.twitch.tv/helix/streams?game_id=1469308723&first=100",
        headers={
            "Authorization": "Bearer " + config("TWITCH_AUTH_TOKEN"),
            "Client-Id": config("TWITCH_CLIENT_ID"),
        },
    )
    streams_data = r_streams.json()["data"]
    streams = [set_stream_properties(s) for s in streams_data]

    tags = Tag.objects.all().order_by("-type", "name")

    for stream in streams:
        title = stream["title"].lower().replace(" ", "")
        stream["tags_names"] = [tag.name for tag in tags if tag.code_name in title]
        stream["tags_codes"] = [tag.code_name for tag in tags if tag.code_name in title]

    cache.set("streams", streams, 60)

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "streams_group", {"type": "streams_list", "message": streams}
    )

    return streams
