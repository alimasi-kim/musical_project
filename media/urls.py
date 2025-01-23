from django.urls import path
from . import views

app_name = 'media'

urlpatterns = [
    path('videos/', views.video_list, name='video_list'),
    path('videos/<slug:slug>/', views.video_detail, name='video_detail'),
    path('photos/', views.photo_list, name='photo_list'),
    path('photos/<slug:slug>/', views.photo_detail, name='photo_detail'),
] 