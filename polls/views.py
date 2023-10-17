from django.http import HttpResponse

def fuktorial(x):
    result = 1
    for i in range(1,x+1,1):
        result = result*i
    return result
def fuktor(request,value):

    return HttpResponse(f"<h1>Факториал {value} = {fuktorial(value)}<h1>")

def def2(request):

    return HttpResponse('привет')