from django.contrib import admin

from . import models

admin.sites.AdminSite.site_header = 'Administração do Events'

# Register your models here.
admin.site.register(models.Evento)