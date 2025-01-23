from django.contrib import admin
from .models import Contact, Newsletter

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent')
    list_filter = ('date_sent',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('date_sent',)
    ordering = ('-date_sent',)

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date_subscribed', 'is_active')
    list_filter = ('date_subscribed', 'is_active')
    search_fields = ('email', 'name')
    list_editable = ('is_active',)
    ordering = ('-date_subscribed',) 