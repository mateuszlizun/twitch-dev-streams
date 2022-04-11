from celery import shared_task
from datetime import datetime
from django.core.cache import cache


@shared_task
def current_date():
    currentDate = datetime.now()
    cache.set("current_date", currentDate, 30)
    return currentDate
