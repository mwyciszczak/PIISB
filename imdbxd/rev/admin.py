from django.contrib import admin

# Register your models here.
from .models import *


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'release_date', 'get_actors', 'get_directors')

    def get_actors(self, obj):
        return "\n".join(['{} {}'.format(a.name, a.surname) for a in obj.actors.all()])

    def get_directors(self, obj):
        return "\n".join(['{} {}'.format(a.name, a.surname) for a in obj.directors.all()])


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rating')


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birthdate')


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birthdate')


admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Entry, EntryAdmin)