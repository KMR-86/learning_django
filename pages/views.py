from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>home page</h1>")
    info = {}
    info["username"] = "mushi"
    info["content"] = "this is the content of the blog"
    info["friendlist"] = ["nishat", "adam", "ben", "tony"]

    return render(request, "home.html", info)


def education_view(request, *args, **kwargs):
    return render(request, "education.html", {})


def achievement_view(request, *args, **kwargs):
    return render(request, "achievement.html", {})


def index_view(request, *args, **kwargs):
    return render(request, "index.html", {})
