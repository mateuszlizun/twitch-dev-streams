from django.core.cache import cache
from django.shortcuts import render


def index(request):
    streams = cache.get("streams")
    return render(request, "streams/index.html", {"streams": streams})
