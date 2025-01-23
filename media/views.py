from django.shortcuts import render, get_object_or_404
from .models import Video, Photo

def media_list(request):
    """Vue principale de la section médias"""
    videos = Video.objects.all().order_by('-date_added')[:3]
    photos = Photo.objects.all().order_by('-date_added')[:6]
    
    return render(request, 'media/media_list.html', {
        'videos': videos,
        'photos': photos,
    })

def video_list(request):
    videos = Video.objects.all().order_by('-date_added')
    return render(request, 'media/video_list.html', {
        'videos': videos
    })

def video_detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'media/video_detail.html', {
        'video': video
    })

def photo_list(request):
    photos = Photo.objects.all().order_by('-date_added')
    return render(request, 'media/photo_list.html', {
        'photos': photos
    })

def photo_detail(request, slug):
    photo = get_object_or_404(Photo, slug=slug)
    return render(request, 'media/photo_detail.html', {
        'photo': photo
    }) 