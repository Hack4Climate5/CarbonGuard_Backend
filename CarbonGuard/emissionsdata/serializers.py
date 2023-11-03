from rest_framework import serializers
from .models import EmissionsData


class EmissionsDataSerializer(serializers.ModelSerializer):
    emission_value = serializers.CharField(source='emissionvalue.emission_value')

    class Meta: 
        model = EmissionsData
        fields = "__all__"