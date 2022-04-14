from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from datetime import datetime
from django.core.cache import cache


@shared_task
def current_date():
    currentDate = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    cache.set("current_date", currentDate, 30)

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "current_date_group", {"type": "date_message", "message": currentDate}
    )

    return currentDate
