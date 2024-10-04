from django.db import models

# Create your models here.
class Artist(models.Model):
    name= models.Charfield(max_length=100)
    
class Album(models.Model):
    title= models.Charfield(max_length=100)
    artist= models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)

class Song(models.Model):
    title= models.Charfield(max_length=100)
    album= models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    
