from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=120)
    profile_bio = models.TextField()
    profile_picture = models.ImageField(upload_to="media/")
    total_friends = models.IntegerField()
