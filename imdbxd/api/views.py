from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .serializers import ActorSerializer, DirectorSerializer, FilmSerializer, EntrySerializer, UserSerializer
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


@api_view(['GET'])
def get_entries(request):
    items = Entry.objects.all()
    serializer = EntrySerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])  # nie działa
def add_entry(request):
    serializer = EntrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

