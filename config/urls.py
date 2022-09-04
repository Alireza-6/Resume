from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('info.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # add static files path to urls
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # add static media's path to urls
