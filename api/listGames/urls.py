from django.urls import path , include
from .views import AllCurrency, ListGamesView , ListGameView

urlpatterns = [
   path('' , ListGamesView.as_view()),
   path('<id>' , ListGameView.as_view()),
   path('currency/all' , AllCurrency.as_view())
]
