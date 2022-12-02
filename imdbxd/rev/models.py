from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models import signals

# Create your models here.


class Actor(models.Model):
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    birthdate = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    birthdate = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=1000, null=True)
    release_date = models.DateTimeField(null=True)
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    slug = models.SlugField(max_length=150, null=True, editable=False)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.username


class Entry(models.Model):
    title = models.ForeignKey(Film, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    rating = models.FloatField(null=True)


@receiver(signals.pre_save, sender=Film)
def populate_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)

# TODO
# Oceny co pół, z listy
# Razem z oceną komentarz usera
# Jak ma wyglądać slug(auto, czy z palca)
# Czy userzy mają być z modeli, czy tam w panelu
# Czy szukanie ocen we wpisach jest viable
# Czy zdjęcia mogą być w bazie, czy staticu
# Czy jest sens w życiu
