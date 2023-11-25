from django.shortcuts import render
from skills.models import Skills


def skills(request):
    skills = Skills.objects.all()
    context = {
        "skills": skills
    }
    return render(request, "pages/skills.html", context)
