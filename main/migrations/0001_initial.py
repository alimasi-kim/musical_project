# Generated by Django 4.2.17 on 2025-01-20 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('bio', models.TextField(verbose_name='Biographie')),
                ('photo', models.ImageField(upload_to='artists/', verbose_name='Photo')),
                ('quote', models.TextField(blank=True, verbose_name='Citation')),
            ],
            options={
                'verbose_name': 'Artiste',
                'verbose_name_plural': 'Artistes',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('date', models.DateTimeField(verbose_name="Date de l'événement")),
                ('location', models.CharField(max_length=200, verbose_name='Lieu')),
                ('image', models.ImageField(blank=True, null=True, upload_to='events/%Y/%m/', verbose_name='Image')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Événement à la une')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Événement',
                'verbose_name_plural': 'Événements',
                'ordering': ['date'],
            },
        ),
    ]
