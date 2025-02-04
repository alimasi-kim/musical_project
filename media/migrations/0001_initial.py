# Generated by Django 4.2.17 on 2025-01-22 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('date', models.DateTimeField(verbose_name="Date de l'événement")),
                ('location', models.CharField(max_length=200, verbose_name='Lieu')),
                ('image', models.ImageField(blank=True, upload_to='events/', verbose_name='Image')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Mis en avant')),
                ('ticket_url', models.URLField(blank=True, verbose_name='Lien de réservation')),
            ],
            options={
                'verbose_name': 'Événement',
                'verbose_name_plural': 'Événements',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/', verbose_name='Image')),
                ('description', models.TextField(verbose_name='Description')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")),
                ('is_featured', models.BooleanField(default=False, verbose_name='Photo à la une')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('video_url', models.URLField(verbose_name='URL de la vidéo')),
                ('thumbnail', models.ImageField(upload_to='videos/thumbnails/', verbose_name='Miniature')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date d\'ajout')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Mis en avant')),
                ('views_count', models.IntegerField(default=0, verbose_name='Nombre de vues')),
            ],
            options={
                'verbose_name': 'Vidéo',
                'verbose_name_plural': 'Vidéos',
                'ordering': ['-date_added'],
            },
        ),
    ]
