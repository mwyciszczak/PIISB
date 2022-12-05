from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.get_actors),
    path('directors/', views.get_directors),
    path('films/', views.get_films),
]