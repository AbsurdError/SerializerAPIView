from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    size = models.CharField(max_length=60)
    manufacturer = models.ManyToManyField('Manufacturer')
    category = models.ManyToManyField('Category')
    price = models.CharField(max_length=7)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=25)

    def __str__(self):
        return self.name