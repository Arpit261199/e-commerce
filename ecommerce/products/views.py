from django.shortcuts import render

from. serializers import* 
from.models import*
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response


class ProductView(APIView):
    
    def get(self,request): 
        queryset =Product.objects.all()
        serializers=ProductSerializers(queryset , many = True)
        return Response(serializers.data)
        
