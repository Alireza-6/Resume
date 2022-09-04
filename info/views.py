from django.shortcuts import render

from .models import (
    SiteSetting,
    Skill,
    Familiarity,
    Worked,
    PersonalInfo,
)


def home(request):
    site_setting = SiteSetting.objects.all().first()
    context = {
        'site_setting': site_setting
    }
    return render(request, 'index.html', context)
