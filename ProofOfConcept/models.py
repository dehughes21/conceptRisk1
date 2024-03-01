from django.db import models
from datetime import datetime

class Squirrel(models.Model):

    name = models.CharField(max_length=30)
    weight = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
class User(models.Model):
    email = models.EmailField('User Email')
    banned = models.BooleanField(blank=True)

    def __str__(self):
        return self.email
    
class Sighting(models.Model):
    time = models.DateTimeField('Sighting Time') # SUBJECT TO CHANGE

    #squirrelID = models.FloatField('Squirrel ID', max_length=50)
    squirrel = models.ForeignKey(Squirrel, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/', blank=True)
    image3 = models.ImageField(upload_to='images/', blank=True)
    image4 = models.ImageField(upload_to='images/', blank=True)
    image5 = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(blank=True)
    # Many-to-many relationship for behaviors?
    
    def __str__(self):
        return self.squirrelID + str(self.time)
    

