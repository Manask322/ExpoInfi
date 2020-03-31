from django.urls import path

# from .views import HomePageView
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('game/<attemps>/<level>',views.game,name='game'),
    path('login/',views.login,name='login'),
    path('start_game/',views.start_game,name='start_game'),
    path('games/',views.games, name='games')
]