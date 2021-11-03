from django.db import models


class Games(models.Model):
    rater = models.ForeignKey("Rater", on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    designer = models.CharField(max_length=55)
    year_released = models.IntegerField()
    num_of_players = models.IntegerField()
    est_time_to_play = models.IntegerField()
    recommended_age = models.IntegerField()