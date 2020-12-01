from django.db import models
from django.db.models.deletion import CASCADE

class Event(models.Model):
    game = models.ForeignKey("Game", on_delete=CASCADE)
    organizer = models.ForeignKey("Gamer", on_delete=CASCADE, related_name="events", related_query_name="event") 
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
