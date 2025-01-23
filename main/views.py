from django.shortcuts import render
from media.models import Video, Event, Photo
from main.models import Artist
from django.utils import timezone
from django.db.models import Count

def home(request):
    """Vue pour la page d'accueil"""
    # Récupérer les 3 dernières vidéos
    latest_videos = Video.objects.filter(
        date_added__lte=timezone.now()
    ).order_by('-date_added')[:3]
    
    # Récupérer les 6 dernières photos
    latest_photos = Photo.objects.filter(
        date_added__lte=timezone.now()
    ).order_by('-date_added')[:6]
    
    # Récupérer les vidéos mises en avant
    featured_videos = Video.objects.filter(
        is_featured=True,
        date_added__lte=timezone.now()
    ).order_by('-date_added')[:2]
    
    # Récupérer les prochains événements
    upcoming_events = Event.objects.filter(
        date__gte=timezone.now()
    ).order_by('date')[:4]
    
    # Statistiques pour la section Stats
    stats = {
        'video_views': Video.objects.count(),  # Temporairement, utilisons juste le nombre de vidéos
        'events_count': Event.objects.count(),
        'videos_count': Video.objects.count(),
    }
    
    # Récupérer les informations de l'artiste
    artist = Artist.objects.first()
    
    context = {
        'latest_videos': latest_videos,
        'latest_photos': latest_photos,
        'featured_videos': featured_videos,
        'upcoming_events': upcoming_events,
        'stats': stats,
        'artist': artist,
    }
    
    return render(request, 'main/home.html', context)

def about(request):
    """Vue pour la page À propos"""
    context = {
        'achievements': [
            {
                'icon': 'fas fa-microphone-alt',
                'number': '150+',
                'label': 'Concerts Donnés'
            },
            {
                'icon': 'fas fa-users',
                'number': '50K+',
                'label': 'Vies Touchées'
            },
            {
                'icon': 'fas fa-compact-disc',
                'number': '200+',
                'label': 'Chants de Louange'
            }
        ],
        'testimonials': [
            {
                'quote': "Une voix qui touche l'âme et élève l'esprit.",
                'author': 'Radio Gospel RDC',
                'role': 'Média Musical'
            },
            {
                'quote': "Un artiste authentique qui inspire toute une génération.",
                'author': 'Festival Gospel de Kinshasa',
                'role': 'Événement Musical'
            }
        ]
    }
    
    return render(request, 'main/about.html', context)

def support(request):
    """Vue pour la page de soutien"""
    # Vous pouvez ajouter des données pour les options de soutien ici
    support_options = {
        'donation_link': '#',  # Lien vers votre système de don
        'social_media': {
            'facebook': 'https://facebook.com/votre-page',
            'twitter': 'https://twitter.com/votre-compte',
            'instagram': 'https://instagram.com/votre-compte'
        }
    }
    
    return render(request, 'main/support.html', {
        'page_title': 'Nous Soutenir',
        'support_options': support_options
    }) 