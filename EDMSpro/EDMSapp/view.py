from django.shortcuts import render

from EDMSapp.models import EDMSmodel
from EDMSapp.serializers import EDMSSerializer
from EDMSapp.pagination import MyPagination 

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status



class EDMSViewSet(viewsets.ModelViewSet):
    queryset = EDMSmodel.objects.all()
    serializer_class = EDMSSerializer
    pagination_class = MyPagination

    
    @action(detail=False, methods=["GET"],url_path='show_all')
    def get_manager(self,request):
        queryset = EDMSmodel.objects.all().order_by('id')
        
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = EDMSSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

     
    @action(detail=False, methods=["GET"],url_path='show')
    def getCustom(self, request):
        queryset = EDMSmodel.objects.all()
        serializer = EDMSSerializer(queryset,many=True) 
        return Response(serializer.data)
    
    @action(detail=True, methods=["GET"],url_path='one_display')  #detail=True & many=false(default) handle single value
    def retriveCustom(self, request,pk=None):
        queryset = EDMSmodel.objects.get(pk=pk)
        serializer = EDMSSerializer(queryset) 
        return Response(serializer.data)
    
    @action(detail=False, methods=["POST"],url_path='create')
    def created(self, request):
        dataReceived = request.data
        serializer = EDMSSerializer(data = request.data)
        
        if EDMSmodel.objects.filter(**dataReceived).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
    @action(detail=True , methods=['PUT'],url_path='modify')
    def modify(self,request,pk=None):
        EDMS = EDMSmodel.objects.get(pk=pk)
        serializer = EDMSSerializer(instance = EDMS,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message':'data is modify'})
    
    @action(detail=True , methods=['PATCH'],url_path='update')
    def updated(self,request,pk=None):
        EDMS = EDMSmodel.objects.get(pk=pk)
        serializer = EDMSSerializer(EDMS,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)
    
    @action(detail=True , methods=['DELETE'],url_path='delete')
    def remove(self,request,pk=None):
        EDMS = EDMSmodel.objects.get(pk=pk)  
        EDMS.delete()
        return Response({'message':'data is delete'})
    
    
    
    

