from django.shortcuts import render

from EDMSapp.models import EDMSmodel , Emp_address
from EDMSapp.serializers import AddressDetailSerializer, EDMSSerializer , EaddSerializer , EmpDetailSerializer
from EDMSapp.pagination import MyPagination 

from rest_framework import viewsets ,status
from rest_framework.response import Response
from rest_framework.decorators import action


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
    
    @action(detail=False,methods=["GET"],url_path='show_null_id')
    def get_null_id(self,request):
        qs= EDMSmodel.objects.filter(manager__isnull = True).values()
        page_num = int(request.GET['page'])
        page_size_num =int(request.GET['page_size'])
        offset =((page_num-1)*page_size_num)
        limit = page_size_num*page_num
        res_page = qs[offset:limit]
        print(res_page)
        serializer = EDMSSerializer(res_page,many=True).data
        return Response(serializer)

     
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
    
    
    @action(detail=False , methods=['DELETE'],url_path='delete_all')
    def remove_all(self,request):
        EDMSmodel.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    
    
class emp_add_viewset(viewsets.ModelViewSet):
    queryset = Emp_address.objects.all()
    serializer_class = EaddSerializer
    
    @action(detail=False , methods=['GET'],url_path='get_add')
    def get_address(self, request ):
        queryset = Emp_address.objects.all()
        serializer = EaddSerializer(queryset,many=True) 
        return Response(serializer.data)
    
    
    @action(detail=False, methods=["POST"],url_path='add_create')
    def Add_created(self, request):
        dataReceived = request.data 
        serializer = EaddSerializer(data = request.data)
        
        if Emp_address.objects.filter(**dataReceived).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
    @action(detail=True , methods=['PUT'],url_path='Add_modify')
    def Addmodify(self,request,pk=None):
        EDMS = Emp_address.objects.get(pk=pk)
        serializer = EaddSerializer(instance = EDMS,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        
    @action(detail=True , methods=['DELETE'],url_path='add_delete')
    def Addremove(self,request,pk=None):
        EDMS = Emp_address.objects.get(pk=pk)  
        EDMS.delete()
        return Response({'message':'data is delete'})
    
class EmpDetailViewSet(viewsets.ReadOnlyModelViewSet):
   
    @action(detail=False , methods=['GET'],url_path='get_all')
    def get_all_detail(self, request ):
        queryset = Emp_address.objects.all()
        serializer = EmpDetailSerializer(queryset, many=True) 
        return Response(serializer.data)
    
    
    @action(detail=False , methods=['GET'],url_path='get_all_emp')
    def get_all_emp_detail(self, request ):
        queryset = EDMSmodel.objects.all()
        serializer = AddressDetailSerializer(queryset, many=True) 
        return Response(serializer.data)