from django.shortcuts import render

# Create your views here.
from EDMSapp.models import EDMSmodel
from EDMSapp.serializers import EDMSSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view



    
@api_view(['GET'])
    # list action
def list(request):
    serializer = EDMSmodel.objects.all()
    if serializer:
        serializer = EDMSSerializer(serializer,many = True)
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)


    
@api_view(['POST'])
def EDMScreate(request):
    # Receive the data from the client side
    dataReceived = request.data
    serializer = EDMSSerializer(data=dataReceived)

    # Check if data already exist or not
    if EDMSmodel.objects.filter(**dataReceived).exists():
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    # Validate the data entered by the user
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
   


@api_view(['PUT'])
    #modify action
def update(request,pk):
    EDMS = EDMSmodel.objects.get(pk= pk)
    serializer = EDMSSerializer(instance=EDMS, data=request.data)
    if serializer.is_valid():
       serializer.save() 
       return Response(serializer.data)
    else: 
        return Response(status= status.HTTP_204_NO_CONTENT)
    

       
@api_view(['PATCH'])
def modify(request, pk):
    EDMS = EDMSmodel.objects.get(pk= pk)
    serializer = EDMSSerializer(instance=EDMS, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
       

@api_view(['DELETE'])
    # destroy action
def destroy(request, pk):
    # getting object
    EDMS = EDMSmodel.objects.get(pk=pk)  
    # student deletion
    EDMS.delete()
    # returning status as response
    return Response(status=status.HTTP_202_ACCEPTED)


