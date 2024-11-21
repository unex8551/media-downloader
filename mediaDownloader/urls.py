from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tiktok-mp3-downloader/', views.tiktok_mp3, name='tiktok-MP3-Downloader'),
    path('instagram-mp4-downloader/', views.instagram_mp4, name='instagram-MP4-Downloader'),
    path('facebook-mp4-downloader/', views.facebook_mp4, name='facebook-MP4-Downloader'),
]