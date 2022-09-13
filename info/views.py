from django.shortcuts import render

from .models import (
    SiteSetting,
    Skill,
    Familiarity,
    Experience,
    PersonalInfo,
)


def home(request):
    site_setting = SiteSetting.objects.all().first()
    personal_info = PersonalInfo.objects.all().first()
    skills = Skill.objects.all()
    familiarities = Familiarity.objects.all()
    experiences = Experience.objects.all()
    context = {
        'site_setting': site_setting,
        'skills': skills,
        'familiarities': familiarities,
        'experiences': experiences,
        'personal_info': personal_info,
    }
    return render(request, 'index.html', context)


def error_404(request, exception):
    context = {}
    return render(request, '404.html', context)
