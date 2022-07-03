
from locale import currency
from .models import Games, Currency
from .serializers import GamesSerializer , CurrencySerializer, SearchGamesSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination 
from mongoengine.queryset.visitor import Q
from rest_framework_mongoengine import viewsets



# Create your views here.
class ListGamesView(viewsets.ModelViewSet):

   
    def get(self,request):
        games = Games.objects.all().order_by('-releaseDate')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(games , request)

        serializer = GamesSerializer(result_page , many=True)
        response = Response(serializer.data , status=status.HTTP_200_OK)
        return response
        
class ListGameView(ListAPIView):
    
    def get(self,request, title):
        print(title)
        game = Games.objects.get(title=title)
        region = request.query_params.get('currency', 'SGD')
        local = Currency.objects.get(id=region)
        localRate = local.rate
        store = game.store
        for key  in store:
            market = store[key]    
            currency = market.get('currency')
            convertionRate = Currency.objects.get(id=currency)
            rates = convertionRate.rate
            if market.get('price') is not None:
                market['price'] = (market.get('price') / float(rates)) *float(localRate)
           
    
        serializer = GamesSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AllCurrency(ListAPIView):
    
    def get(self ,request):
        allCurrency = Currency.objects.all()
        serializer = CurrencySerializer(allCurrency , many =True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
class SearchGame(ListAPIView):
  
    serializer_class = SearchGamesSerializer
    
    def get_queryset(self):
        searchTerm = self.request.query_params.get('search')
        games = Games.objects.filter(Q(title__icontains=searchTerm) & Q(imageUrl__ne=None))
        titles = set()
        newlist = [i for i in games if i.title not in titles and titles.add(i.title) is None]

        return newlist