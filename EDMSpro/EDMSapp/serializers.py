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


class DetailIDSerializer(serializers.ModelSerializer):
    addres = serializers.SerializerMethodField()

    class Meta:
        model = EDMSmodel
        fields = ('name', 'id', 'roll_no', 'addres')
        
    def get_addres(self,obj):            #this fun is defind becoz of EDMSmodel don't know about address (but address know about EDMSmodel)
        print(obj)
        address= obj.address.filter(emp_model=obj.id)
        address_serializer = EaddSerializer(address, many=True)
        return address_serializer.data
