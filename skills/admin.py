from django.contrib import admin
from skills.models import Skills


class SkillsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Skills, SkillsAdmin)
