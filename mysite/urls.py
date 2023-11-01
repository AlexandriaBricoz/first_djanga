from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from mysite import settings

from polls.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", include('polls.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documen_root=settings.MEDIA_ROOT)
handler404 = pageNotFound
