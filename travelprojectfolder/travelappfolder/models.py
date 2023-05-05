from django.db import models


# Create your models here.
class travelgram(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    descr = models.TextField()


class teams(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=350)
