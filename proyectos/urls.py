from django.urls import path
from .views import projects


urlpatterns = [
    path('projects/',projects, name="projects"),    
]

from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
