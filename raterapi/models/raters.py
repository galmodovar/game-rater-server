from django.db import models
from django.contrib.auth.models import User

class Rater(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_url = models.ImageField()