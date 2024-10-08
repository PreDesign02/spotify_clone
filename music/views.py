# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.object.all()
    serializer_class= ArtistSerializer
    
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.object.all()
    serializer_class= AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.object.all()
    serializer_class= SongSerializer
