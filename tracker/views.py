# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    context = {}
    return render(request, 'tracker/index.html', context)


def createUser(request):
    user = User.objects.create_user(
        request.inputUsername,
        request.inputPassword
    ) 

    context = {
        "success": "Successfully created user"
    }

    return render(request, 'tracker/index.html', context)
