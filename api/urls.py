from django.urls import path
from .views import CreatePlayer, GetUpdatePlayer, ListPlayers

app_name = 'api'

urlpatterns = [
    path('v1/player/', CreatePlayer.as_view()),
    path('v1/player/<player_id>/', GetUpdatePlayer.as_view()),
    path('leaderboards', ListPlayers.as_view()),
]