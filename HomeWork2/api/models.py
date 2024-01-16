from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=25)
    rel_year = models.PositiveIntegerField(max_length=4)
    country = models.CharField(max_length=15)
    director = models.ManyToManyField('Director')
    style = models.ManyToManyField('Style')

    def __str__(self):
        return self.title

class Director(models.Model):
    name = models.CharField(max_length=40)
    birth_year = models.PositiveIntegerField(max_length=4)

    def __str__(self):
        return self.name

class Style(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Poster(models.Model):
    date = models.DateField()
    film = models.ManyToManyField('Film')

