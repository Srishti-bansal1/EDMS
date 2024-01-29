from .models import EDMSmodel ,Emp_address
from rest_framework import serializers

class EDMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = EDMSmodel
        fields = ('id','name', 'roll_no','email','manager')


class EaddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp_address
        fields = ('emp_model','state','city','pin')
        
        
class EmpDetailSerializer(serializers.ModelSerializer):
    emp_model = EDMSSerializer(read_only=True)

    class Meta:
        model = Emp_address
        fields = ('__all__')


class AddressDetailSerializer(serializers.ModelSerializer):
    address = EaddSerializer(read_only=True, many=True)

    class Meta:
        model = EDMSmodel
        fields = ('__all__')
