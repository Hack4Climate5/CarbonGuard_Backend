from django.contrib import admin
from .models import Limit


class LimitAdmin(admin.ModelAdmin):
    list_display = ("emission_limit", 'created_at', 'updated_at')


admin.site.register(Limit, LimitAdmin)
