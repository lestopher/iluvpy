# Create your views here.
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'tracker/index.html', context)