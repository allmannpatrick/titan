from django.db import models
from django.conf import settings


class Post(models.Model):
    cover = models.ImageField(upload_to='images/')


    #def __str__(self):
    #    return self.title
