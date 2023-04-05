from django.urls import path
from django.http import HttpResponse


def my_view(request):
    return HttpResponse('UM LINDA STRING')
def home(request):
    return HttpResponse('HOME')


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')


urlpatterns = [
    path('outra-coisa-qualquer/', my_view),
    path('', home),  # Home
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contato/
]
