from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse
from .forms import Loginform
from django.contrib.auth.views import login


def home(request):
    t = get_template('login/loginsuccess.html')
    return HttpResponse(t.render({}, request))



