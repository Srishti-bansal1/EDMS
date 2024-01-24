from EDMSapp.models import EDMSmodel
from rest_framework import serializers

class EDMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = EDMSmodel
        fields = ('id', 'name', 'roll_no','email','manager')