from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return (self.first_name + ' ' + self.last_name)
        else:
            return self.first_name

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=255, null=False, blank=False)
    likes = models.ManyToManyField(User, null=True, blank=True)
    date_released = models.DateField()

    def __str__(self):
        return self.title

class Lyric(models.Model):
    song = models.ForeignKey(Song, verbose_name='song', related_name='song_lyrics', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.song.title
