from django.db import models
from django.utils.text import slugify

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(verbose_name="Description")
    date = models.DateTimeField(verbose_name="Date de l'événement")
    location = models.CharField(max_length=200, verbose_name="Lieu")
    image = models.ImageField(
        upload_to='events/%Y/%m/', 
        blank=True, 
        null=True, 
        verbose_name="Image"
    )
    is_featured = models.BooleanField(default=False, verbose_name="Événement à la une")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Événement"
        verbose_name_plural = "Événements"
        ordering = ['date']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    bio = models.TextField(verbose_name="Biographie")
    photo = models.ImageField(upload_to='artists/', verbose_name="Photo")
    quote = models.TextField(verbose_name="Citation", blank=True)
    
    class Meta:
        verbose_name = "Artiste"
        verbose_name_plural = "Artistes"
    
    def __str__(self):
        return self.name 