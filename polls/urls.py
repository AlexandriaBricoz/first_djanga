from django.urls import path

from .views import *

urlpatterns = [
    path('<int:value>/',fuktor),
    path('def2/',def2),
    path('sum/',summ),
    path('', main)
]
