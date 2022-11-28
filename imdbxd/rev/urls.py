from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('reviews/', views.reviews),
]