from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import  ListAPIView, UpdateAPIView
from .models import *
from .serializers import *

# Create your views here.
# List All Song
@api_view(['GET'])
def songList(request):
    song = Song.objects.all()
    serializer = SongSerializer(song, many=True)
    return Response(serializer.data, status=200)

# Request for a Song
@api_view(['GET'])
def songDetails(request, pk):
    song = Song.objects.get(id=pk)
    serializer = SongSerializer(song, many=False)
    return Response(serializer.data, status=200)

# Class Based View For Update Song
class updateSong(UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = UpdateSongSerializer
    lookup_field = 'pk'

# Delete a song
@api_view(['DELETE'])
def deleteSong(request, pk):
    song = Song.objects.get(id=pk)
    song.delete()
    message = "Song Deleted successfully"
    return HttpResponse(message,status=200)