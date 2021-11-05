from django.db import models

class Reviews(models.Model):
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    rater = models.ForeignKey("Rater", on_delete=models.CASCADE)
    review = models.TextField()
    created_on = models.DateField()