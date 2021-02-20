from django.contrib import admin
from . models import Pgs


class PgsAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'category')


admin.site.register(Pgs, PgsAdmin)
