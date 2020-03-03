from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'index.html', data)
