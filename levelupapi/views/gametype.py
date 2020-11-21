from django.http import HttpResponseServerError
from django.views.generic.base import View
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from levelupapi.models import GameType

class GameTypesViewSet(ViewSet):
    """Level up game types"""

    def retrieve(self, request, pk=None):
        """ Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        
        try:
            game_type = GameType.objects.get(pk=pk)
            serializer = GameTypeSerializer(game_type, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        
        gametypes = GameType.objects.all()

        # Note the additional 'many=True' argument to the 
        # serializer. It's needed when you are serializin 
        # a list of objects instead of a single object.
        
        serializer = GameTypeSerializer(gametypes, many=True, context={'request': request})
        return Response(serializer.data)
            

class GameTypeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for game types

    Arguments:
        serializers
    """
    
    class Meta:
        model = GameType
        url = serializers.HyperlinkedIdentityField(
            view_name='gametype',
            lookup_field='id'
        )
        fields = ('id', 'url', 'label')
