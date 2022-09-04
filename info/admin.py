from django.contrib import admin

from .models import (
    SiteSetting,
    Skill,
    Familiarity,
    Worked,
    PersonalInfo,
)

admin.site.register(SiteSetting)
admin.site.register(Skill)
admin.site.register(Familiarity)
admin.site.register(Worked)
admin.site.register(PersonalInfo)
