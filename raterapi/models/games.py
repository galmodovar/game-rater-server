from django.db import models
from raterapi.models.game_ratings import GameRatings


class Games(models.Model):
    rater = models.ForeignKey("Rater", on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    designer = models.CharField(max_length=55)
    year_released = models.IntegerField()
    num_of_players = models.IntegerField()
    est_time_to_play = models.IntegerField()
    recommended_age = models.IntegerField()
    


    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        try:
            ratings = GameRatings.objects.filter(game=self)

            # Sum all of the ratings for the game
            total_rating = 0
            for rating in ratings:
                total_rating += rating.rating
                
            return total_rating/len(ratings)
        except:
            return "No ratings"

        
