from django.db import models

from django.utils import timezone


# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now, blank=True)
    creator = models.CharField(max_length=60)
    likes = models.IntegerField()
