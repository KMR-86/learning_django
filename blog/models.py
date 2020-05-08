from django.db import models

from datetime import datetime
from django.utils import timezone
import pytz

# Create your models here.
class blog(models.Model):
    title = models.TextField()
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now, blank=True)
    creator = models.TextField()
