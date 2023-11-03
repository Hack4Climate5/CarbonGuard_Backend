from django.db import models
from vehicles.models import Vehicle


class EmissionsData(models.Model):
    # emissionvalue = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    emissionvalue = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)

    year = models.PositiveIntegerField(null=True, blank=True)
    vehicle_model = models.CharField(max_length=32,null=True)
    chassis_number = models.CharField(max_length=32,null=True)
    engine_type = models.CharField(max_length=32,null=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return f"{self.vehicle_model}"
    
    def get_emission_value(self):
        return self.emissionvalue.emission_value