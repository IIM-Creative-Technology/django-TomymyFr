from django.db import models

# Create your models here.

# create a article with a image, a price, a description and a name
class Article(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name