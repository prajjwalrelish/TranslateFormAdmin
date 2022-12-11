import uuid

from django.db import models
from pytz import timezone


class UUIDMixin(models.Model):
    """ Reusable uuid field"""

    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
    )
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True


