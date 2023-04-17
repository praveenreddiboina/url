from django.db import models

# Create your models here.
class Url(models.Model): # creating class and giving it two objects as follows.
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
