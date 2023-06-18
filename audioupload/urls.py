from django.urls import path
from . import views

urlpatterns = [
    path('api/upload/', views.upload_audio, name='upload_audio'),
     path('api/audio/<str:title>/', views.get_audio_by_title, name='get_audio_by_title'),
]
