from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from mysite import settings

from polls.views import *

urlpatterns = [
    path('', def2),
    path("admin/", admin.site.urls),
    path("catalog/", include('polls.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documen_root=settings.MEDIA_ROOT)
handler404 = pageNotFound
