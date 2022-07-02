from rest_framework_mongoengine import serializers

from .models import Games , Currency

class GamesSerializer (serializers.DocumentSerializer):
    class Meta:
        model = Games
        fields = '__all__'
        
class CurrencySerializer(serializers.DocumentSerializer):
    class Meta:
        model = Currency
        fields = '__all__'
        
class SearchGamesSerializer (serializers.DocumentSerializer):
    class Meta:
        model = Games
        fields = ['title' , 'imageUrl']