from django.urls import path
from tic_tac_toe.views import playgame







urlpatterns=[path('game', playgame, name='game')]
