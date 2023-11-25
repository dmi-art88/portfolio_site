from django.shortcuts import render
from bio.models import Bio
from skills.models import Skills


def bio(request):
    bio = Bio.objects.all()
    context = {
        "bio": bio
    }
    return render(request, "pages/bio.html", context)


def skills(request):
    skills = Skills.objects.all()
    context = {
        "skills": skills
    }
    return render(request, "pages/skills.html", context)
