from django.contrib import admin
from django.urls import include, path
from polls.views import *

urlpatterns = [
    path('',def2),
    path("admin/", admin.site.urls),
    path("catalog/", include('polls.urls')),
]