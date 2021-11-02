from django.db import models


class GameCategories(models.Model):
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    category = models.ForeignKey("Categories", on_delete=models.CASCADE)