from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>home page</h1>")
    return render(request, "home.html", {})


def education_view(request,*args, **kwargs):
    return render(request, "education.html", {})


def achievement_view(request,*args, **kwargs):
    return render(request, "achievement.html", {})
