from django.contrib import admin

from .models import (
    SiteSetting,
    Skill,
    Familiarity,
    Experience,
    PersonalInfo,
)

admin.site.register(SiteSetting)
admin.site.register(Skill)
admin.site.register(Familiarity)
admin.site.register(Experience)
admin.site.register(PersonalInfo)
