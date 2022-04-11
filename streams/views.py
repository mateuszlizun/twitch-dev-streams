from django.core.cache import cache
from django.shortcuts import render


def index(request):
    currentDate = cache.get("current_date", "current date not available")
    return render(request, "streams/index.html", {"current_date": currentDate})
