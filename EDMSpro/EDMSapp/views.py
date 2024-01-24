from django.shortcuts import render

# Create your views here.
from EDMSapp.models import EDMSmodel
from rest_framework import viewsets

from EDMSapp.serializers import EDMSSerializer
from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view

class EDMSViewSet (viewsets.ModelViewSet):
    emp = EDMSmodel.objects.all()
    seralizer_class = EDMSSerializer
    
@api_view(['POST'])
def create(self, request, *args, **kwargs):
    # retrieving the data of the request
    serializer = self.get_serializer(data=request.data)
    # raising exception if it invalid
    serializer.is_valid(raise_exception=True)
    # saving
    serializer.save(serializer)
    # returning data and status as a response
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
    # list action
def list(self, request):
    serializer = self.get_serializer(self.get_queryset(), many=True)
    return self.get_paginated_response(self.paginate_queryset(serializer.data))

    # retrieve action
def retrieve(self, request, pk):
    # getting object
    EDMS = self.get_object()
    serializer = self.get_serializer(EDMS)
    # returning data as response
    return Response(serializer.data)

@api_view(['PUT'])
    #modify action
def update(self,request,pk):
    EDMS = self.get_object(pk= pk)
    serializer = self.get_serializer(EDMS)
    serializer.is_valid(raise_exception=True)
    serializer.save() 
    return Response(serializer.data , status= status.HTTP_204_NO_CONTENT)
       

@api_view(['DELETE'])
    # destroy action
def destroy(self, request):
    # getting object
    EDMS = self.get_object()
    # student deletion
    EDMS.delete()
    # returning status as response
    return Response(status=status.HTTP_204_NO_CONTENT)

