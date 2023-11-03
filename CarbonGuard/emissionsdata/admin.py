from django.contrib import admin
from .models import EmissionsData
# Register your models here.


class EmissionsDataAdmin(admin.ModelAdmin):
    list_display = ('emissionvalue', 'year', 'vehicle_model','chassis_number','engine_type')
    list_filter = ('emissionvalue__id',) 
    # def get_emissionvalue_id(self, obj):
    
    
admin.site.register(EmissionsData, EmissionsDataAdmin)