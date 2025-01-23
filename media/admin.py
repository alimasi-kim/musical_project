from django.contrib import admin
from .models import Video, Photo

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'is_featured')
    list_filter = ('date_added', 'is_featured')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_featured',)
    ordering = ('-date_added',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'is_featured')
    list_filter = ('date_added', 'is_featured')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_featured',)
    ordering = ('-date_added',) 