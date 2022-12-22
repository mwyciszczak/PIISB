from rest_framework import serializers
from rev.models import Actor, Director, Film, Entry
from django.contrib.auth.models import User


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
        depth = 1  # lmao,2h szukania


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
        depth = 2


class UserSerializer(serializers.ModelSerializer):
    # działa aż za bardzo bo wysyła hash hasła XD
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
