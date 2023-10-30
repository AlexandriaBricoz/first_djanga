from django.http import HttpResponse, HttpResponseNotFound, Http404


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
    response = open('my_html/main.html')
    html_doc = response.read()
    return HttpResponse(f"{html_doc}")


def def2(request):
    return HttpResponse('привет')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'страница не найдена')
