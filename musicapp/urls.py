from django.urls import path
from .views import *

urlpatterns = [
    path('', songList, name='song-list'),
    path('song/<str:pk>/', songDetails, name='song-detail'),
    path('update/<str:pk>/', updateSong.as_view(), name='song-update'),
    path('delete-song/<str:pk>/', deleteSong, name='delete-song'),
]