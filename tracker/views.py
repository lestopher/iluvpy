# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.utils.timezone import utc
from datetime import datetime
from django.http import HttpResponse

from tracker.models import Weight, Goal


def index(request):
    context = {}
    return render(request, 'tracker/index.html', context)


def createUser(request):
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    name = request.POST["name"]
    first_name = name.split(' ', 1)[0]
    last_name = name.split(' ', 1)[1]
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    ) 

    messages.success(request, "Successfully created user.")
    context = RequestContext(request, {})

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/tracker/dashboard', context)
    else:
        return redirect('/tracker', context)


@login_required
def dashboard(request):
    name = request.user.get_full_name()
    try:
        goal = Goal.objects.filter(user_id=request.user).latest('date_entered')
    except:
        goal = None

    context = RequestContext(request, {
        "name": name,
        "goal": goal
     })
    return render(request, 'tracker/dashboard.html', context)


def auth(request):
    username = request.POST["username"]
    password = request.POST["password"]

    if request.POST["next"]:
        next = request.POST["next"]
    else:
        next = "/tracker/dashboard"

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        context = RequestContext(request, {})
        return redirect(next, context)
    else:
        messages.error(request, "Couldn't authenticate.")
        context = RequestContext(request, {})
        return render(request, 'accounts/login', context)


def userLogout(request):
    logout(request)
    context = RequestContext(request, {})
    messages.success(request, "Successfully logged out.")
    return redirect('/tracker', context)


# AJAX methods
def setGoalWeight(request):
    if request.user.is_authenticated:
        result = []
        try:
            goal = Goal(
                user_id=request.user,
                goal_weight=request.POST["goalWeight"],
                date_entered=datetime.utcnow().replace(tzinfo=utc)
            )
            goal.save()
        except Exception as e:
            result.append({"valid": False, "message": e.message, "type": type(e).__name__})
        else:
            result.append({"valid": True, "data": {}})
    else:
        result = []
        result.appened({"valid": False, "message": "You must be logged in."})

    return HttpResponse(simplejson.dumps(result), content_type="application/json")
