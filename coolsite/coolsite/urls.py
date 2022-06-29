from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from coolsite import settings
from women.views import *
from django.urls import include

urlpatterns = [
    path('', WomenHome.as_view()),
    path('admin/', admin.site.urls),
    path('', include('women.urls')),# это стоаница сайт 127.1/women/


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

handler404 = pageNotFound