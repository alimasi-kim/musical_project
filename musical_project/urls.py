from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin URL doit être en premier
    path('admin/', admin.site.urls),
    
    # URLs des applications
    path('', include(('main.urls', 'main'), namespace='main')),
    path('media/', include(('media.urls', 'media'), namespace='media')),
    path('contacts/', include(('contacts.urls', 'contacts'), namespace='contacts')),
]

# Servir les fichiers media en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 