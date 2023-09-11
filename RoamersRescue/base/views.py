from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    posts = [{'location':'Poland, Lublin',
             'description': 'aoboasdkasdoasdsasdasdasdasdasdas',
             'accomodates': '1',
             'host': 'abiba'}
             ]
    return render(request, 'home.html', {'posts': posts})