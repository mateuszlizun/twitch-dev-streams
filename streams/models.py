from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    class Type(models.TextChoices):
        LANGUAGE = "LG", _("Language")
        TOPIC = "TP", _("Topic")

    type = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.LANGUAGE,
    )

    name = models.CharField(max_length=50)
    code_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
