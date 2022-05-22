from decimal import Decimal
from locale import currency
from .models import Games, Currency
from .serializers import GamesSerializer , CurrencySerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination 


# Create your views here.
class ListGamesView(ListAPIView):
   
    def get(self,request):
        games = Games.objects.all().order_by('-releaseDate')
        region = request.query_params.get('currency', 'SGD')
        local = Currency.objects.get(id=region)
        localRate = local.rate
         
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(games , request)
      
        for game in result_page:
            
            currency = game.currency
            convertionRate = Currency.objects.get(id=currency)
            rates = convertionRate.rate
            # divide first then mutiply
            if game.lowestPrice is not None:
                game.lowestPrice = (game.lowestPrice / rates) *localRate
            if game.msrp is not None:
                game.msrp = (game.msrp / rates) *localRate
            if game.currentPrice is not None:
                game.currentPrice = (game.currentPrice /rates)*localRate
        
        serializer = GamesSerializer(result_page , many=True)
        response = Response(serializer.data , status=status.HTTP_200_OK)
        return response
        
class ListGameView(ListAPIView):
    
    def get(self,request,id):
        game = Games.objects.get(id=id)
        region = request.query_params.get('currency', 'SGD')
        local = Currency.objects.get(id=region)
        localRate = local.rate
        currency = game.currency
        convertionRate = Currency.objects.get(id=currency)
        rates = convertionRate.rate
        if game.lowestPrice is not None:
            game.lowestPrice = (game.lowestPrice / rates) *localRate
        if game.msrp is not None:
            game.msrp = (game.msrp / rates) *localRate
        if game.currentPrice is not None:
            game.currentPrice = (game.currentPrice /rates)*localRate
       
        
        serializer = GamesSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AllCurrency(ListAPIView):
    
    def get(self ,request):
        allCurrency = Currency.objects.all()
        serializer = CurrencySerializer(allCurrency , many =True)
        return Response(serializer.data , status=status.HTTP_200_OK)