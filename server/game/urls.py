from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_game),
    path('<int:game_id>/guess/', views.guess_number),
]
