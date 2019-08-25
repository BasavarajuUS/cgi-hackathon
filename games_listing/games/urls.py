from django.conf.urls import url
from .views import GameView, GameSearchView, home


urlpatterns = [
    url(r'^$', home, name='index'),
    url(r'^api/v1/games/$', GameView.as_view(), name='games'),
    url(r'^api/v1/games/(?P<game_id>\d+)/$', GameView.as_view(), name='game'),
    url(r'^api/v1/games/search/$', GameSearchView.as_view(), name='game-search'),
]

