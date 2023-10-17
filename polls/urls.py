from django.urls import path

from .views import *

urlpatterns = [
    path('fuktor/<int:value>/',fuktor),
    path('def2/',def2)
]
