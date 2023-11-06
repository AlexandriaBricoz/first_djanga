from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('articles/', article, name='articles'),
    path('add/', add_article, name='add_article'),
    path('article/<int:art_id>/', show_article, name='article'),
    path('successful_add/', successful_add, name='successful'),
    path('test/', test, name='test'),
]
