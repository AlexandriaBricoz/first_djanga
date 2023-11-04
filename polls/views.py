from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import *

menu = [
    {'title': 'Home', 'url_name': 'home'},
    {'title': 'Articles', 'url_name': 'articles'},
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add article', 'url_name': 'add_article'},
]


def home(request):
    return render(request, 'polls/home.html', {'title': 'Главная страница', 'menu': menu})


def about(request):
    return render(request, 'polls/about.html', {'title': 'O нас', 'menu': menu})


def article(request):
    articles = Article.objects.all()
    return render(request, 'polls/articles.html', {'articles': articles, 'title': 'Мои статьи', 'menu': menu})


def add_article(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': 'Создать статью',
        'menu': menu,
        'home': menu[0]['url_name']
    }
    return render(request, 'polls/add_article.html', context=context)


def show_article(request, art_id):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': 'Статья',
        'menu': menu,
        'article': articles[art_id - 1]
    }
    return render(request, 'polls/article.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'страница не найдена')


def successful_add(request):
    title = request.GET['title']
    content = request.GET['content']
    new_article = Article(title=title, content=content)
    new_article.save()
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': title,
        'menu': menu,
        'content': content
    }
    return render(request, 'polls/suссessful_add.html', context=context)
