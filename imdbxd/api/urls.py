from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.get_actors),
    path('directors/', views.get_directors),
    path('films/', views.get_films),
    path('entries/', views.get_entries),
    path('add_entry/', views.add_entry),
]