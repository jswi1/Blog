from django.shortcuts import render
from .models import *

def home(request):
    return render(request, "home.html")

def blog(request):
    maqolalar = Maqola.objects.all()
    data = {
        "maqolalar":maqolalar
    }
    return render(request, "blog.html")

def about(request):
    return render(request, "about.html")

def maqola(request):
    return render(request, "maqola.html")