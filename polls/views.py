from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from .models import *


def fuktorial(x):
    result = 1
    for i in range(1, x + 1, 1):
        result = result * i
    return result


def summ(request):
    if request.GET:
        try:
            value1 = int(request.GET['i'])
            value2 = int(request.GET['k'])
        except:
            raise Http404()
    return HttpResponse(f"<h1>{value1}+{value2} = {value1 + value2}<h1>")


def fuktor(request, value):
    return HttpResponse(f"<h1>Факториал {value} = {fuktorial(value)}<h1>")


def main(request):
    return render(request, 'polls/mask.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'polls/about.html', {'title': 'O нас'})


def article(request):
    # objects
    articles = Article.objects.all()
    return render(request, 'polls/article.html', {'articles': articles, 'title': 'Мои статьи'})


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'страница не найдена')
