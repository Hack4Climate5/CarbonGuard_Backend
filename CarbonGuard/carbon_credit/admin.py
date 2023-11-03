from django.contrib import admin
from .models import CarbonCredits


class CarbonCreditsAdmin(admin.ModelAdmin):
    list_display = ('emission_data', 'emission_limit','credit_earned')
    list_filter = ('emission_data__vehicle_model', 'emission_limit__emission_limit')  # Use 'vehicle_model' from the related EmissionsData
    search_fields = ('emission_data__vehicle_model',) 
    
    
admin.site.register(CarbonCredits, CarbonCreditsAdmin)