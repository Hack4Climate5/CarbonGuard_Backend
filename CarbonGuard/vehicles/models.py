from django.db import models
from decimal import Decimal


class Vehicle(models.Model):
    emission_value = models.DecimalField(decimal_places=2, max_digits=14, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return str(self.emission_value)

    def convert_emissions(self):
        converted_emissions = (Decimal('44.01') * Decimal(str(self.emission_value))) / Decimal('24.45')
        gas_equivalent = converted_emissions / Decimal('1000000')
        return gas_equivalent
    
    def save(self, *args, **kwargs):
        self.emission_value = self.convert_emissions()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "vehicle_table"