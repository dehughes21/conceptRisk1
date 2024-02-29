from django.db import models

class Squirrel(models.Model):

    name = models.CharField(max_length=30)
    weight = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name