from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings

class Gamer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    bio = models.CharField(max_length=50)
