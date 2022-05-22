from rest_framework import serializers
from .models import Games , Currency

class GamesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = '__all__'
        
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id']