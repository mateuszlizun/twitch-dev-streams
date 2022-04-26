from django.core.cache import cache
from django.shortcuts import render

from .utils import set_stream_properties
from .models import Tag


def index(request):
    streams_data = cache.get("streams")
    streams = []

    if streams_data:
        streams = [set_stream_properties(s) for s in streams_data]

    tags = Tag.objects.all().order_by("-type", "name")

    return render(
        request,
        "streams/index.html",
        {
            "streams": streams,
            "tags": tags,
        },
    )
