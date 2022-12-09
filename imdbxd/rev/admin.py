from django.contrib import admin

# Register your models here.
from .models import *


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'release_date')


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
