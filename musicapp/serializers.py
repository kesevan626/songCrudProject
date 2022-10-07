from rest_framework import serializers
from .models import *

class SongSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Song
        fields = ['id','title', 'artist', 'likes', 'date_released']

class UpdateSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'artist','date_released']