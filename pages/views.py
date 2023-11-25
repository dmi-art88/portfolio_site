from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html", {})


def bio(request):
    return render(request, "pages/bio.html", {})


def skills(request):
    return render(request, "pages/skills.html", {})
