from unicodedata import category

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Tatoo


def home(request):
    tatoos = Tatoo.objects.all().order_by('id')
    return render(request, 'home/pages/home.html', context={
        'tatoos': tatoos,
    })


def galeria(request, id):
    tatoos = Tatoo.objects.filter(categoria__id=id).order_by('-id')
    return render(request, 'home/pages/home-galeria.html', context={
         'categoria': tatoos,
    })
