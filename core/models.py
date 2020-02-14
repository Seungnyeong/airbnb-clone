from django.db import models
from . import manager

# Create your models here.


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = manager.CustomModelManager()

    class Meta:
        abstract = True
