from django.db import models


class Picture(models.Model):
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    rater = models.ForeignKey("Rater", on_delete=models.CASCADE)
    image_url = models.ImageField()