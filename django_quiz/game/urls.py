import django
from django.urls import path
from .views import game, step, retire, failTime

urlpatterns = [
    path('<int:level>', game, name='game_process'),
    path('step', step),
    path('retire/<int:level>', retire),
    path('failtime', failTime),
]