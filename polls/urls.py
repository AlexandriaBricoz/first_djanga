from django.urls import path

from .views import *

urlpatterns = [
    path('<int:value>/', fuktor),
    path('sum/', summ),
    path('', main),
    path('about/', about),
    path('article/', article)
]
