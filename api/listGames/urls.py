from django.urls import path , include
from .views import AllCurrency, ListGamesView , ListGameView, SearchGame

urlpatterns = [
   path('' , ListGamesView.as_view({'get': 'get'})),
   path('<title>' , ListGameView.as_view()),
   path('currency/all' , AllCurrency.as_view()),
   path('searchGames/' , SearchGame.as_view())
   
]
