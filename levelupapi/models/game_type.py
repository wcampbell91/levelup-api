from django.db import models
from django.db.models.deletion import CASCADE

class Game_type(models.Model):
    label = models.CharField(max_length=55)
