from django.contrib import admin
from .models import Vehicle

# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('emission_value','created_at','updated_at')
admin.site.register(Vehicle, VehicleAdmin)

    