from django.contrib import admin
from bio.models import Bio


class BioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bio, BioAdmin)
