from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .serializers import ActorSerializer, DirectorSerializer, FilmSerializer
from rev.models import Actor, Director, Film, Entry


@api_view(['GET'])
def get_actors(request):
    items = Actor.objects.all()
    serializer = ActorSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_directors(request):
    items = Director.objects.all()
    serializer = DirectorSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_films(request):
    items = Film.objects.all()
    serializer = FilmSerializer(items, many=True)
    return Response(serializer.data)
