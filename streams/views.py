from django.core.cache import cache
from django.shortcuts import render

from .utils import set_stream_properties


def index(request):
    streams_data = cache.get("streams")
    streams = [set_stream_properties(s) for s in streams_data]

    return render(request, "streams/index.html", {"streams": streams})
