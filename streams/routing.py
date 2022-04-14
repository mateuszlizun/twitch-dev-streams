from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path("ws/current-date/", consumers.CurrentDateConsumer.as_asgi()),
]
