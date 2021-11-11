from django.db import models
from django.db.models.deletion import CASCADE

class GameRatings(models.Model):
    game = models.ForeignKey("Games", on_delete=CASCADE)
    rater = models.ForeignKey("Rater", on_delete=CASCADE)
    rating = models.IntegerField()