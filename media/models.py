from django.db import models
from django.utils.text import slugify

class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name="Description")
    video_url = models.URLField(verbose_name="URL de la vidéo")
    thumbnail = models.ImageField(upload_to='videos/thumbnails/', verbose_name="Miniature")
    date_added = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False, verbose_name="Mis en avant")
    views_count = models.IntegerField(default=0, verbose_name="Nombre de vues")
    
    class Meta:
        ordering = ['-date_added']
        verbose_name = "Vidéo"
        verbose_name_plural = "Vidéos"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_youtube_id(self):
        if "youtu.be" in self.video_url:
            return self.video_url.split('/')[-1]
        elif "youtube.com" in self.video_url:
            return self.video_url.split('v=')[-1].split('&')[0]
        return None

class Photo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/', verbose_name="Image")
    description = models.TextField(verbose_name="Description")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")
    is_featured = models.BooleanField(default=False, verbose_name="Photo à la une")
    
    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ['-date_added']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title 

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name="Description")
    date = models.DateTimeField(verbose_name="Date de l'événement")
    location = models.CharField(max_length=200, verbose_name="Lieu")
    image = models.ImageField(upload_to='events/', verbose_name="Image", blank=True)
    is_featured = models.BooleanField(default=False, verbose_name="Mis en avant")
    ticket_url = models.URLField(verbose_name="Lien de réservation", blank=True)
    
    class Meta:
        ordering = ['date']
        verbose_name = "Événement"
        verbose_name_plural = "Événements"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.date.strftime('%d/%m/%Y')}" 