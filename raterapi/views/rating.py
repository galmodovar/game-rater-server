"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from datetime import date
from rest_framework import serializers
from django.contrib.auth.models import User
from raterapi.models import Games, Rater, Reviews, GameRatings
from raterapi.views.game import GameSerializer

class RatingsView(ViewSet):
    """Game Rater Games"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """

        rater = Rater.objects.get(user=request.auth.user)
        game = Games.objects.get(pk=request.data['gameId'])

        try:
            rating = GameRatings.objects.create(
                rater=rater,
                game = game,
                rating=request.data['rating'],
            )
            serializer = RatingSerializer(rating, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        try:
            rating = GameRatings.objects.get(pk=pk)
            serializer = RatingSerializer(rating, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            rating = GameRatings.objects.get(pk=pk)
            rating.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except GameRatings.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        rating = GameRatings.objects.all()
        
  

        serializer = RatingSerializer(
            rating, many=True, context={'request': request})
        return Response(serializer.data)




class RatingSerializer(serializers.ModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """
    
  
    class Meta:
        model = GameRatings
        fields = ('id', 'game', 'rater', 'rating')

