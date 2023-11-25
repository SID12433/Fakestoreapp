from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from store.models import Category,Product
from store.serializers import CategorySerializer,ProductSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import authentication
from rest_framework import permissions


class UserCreationView(APIView):  
    
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class CategoryView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def create(self,request,*args,**kwargs):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def list(self,request,*args,**kwargs):
        qs= Category.objects.all()
        serializer=CategorySerializer(qs, many=True)
        return Response(serializer.data)
    
    def retrieve(self,*args,**kwargs):
        id = kwargs.get("pk")
        qs = Category.objects.get(id=id)
        serializer=CategorySerializer(qs)
        return Response(data=serializer.data)
    
    def update(self, request,*args,**kwargs):
        id = kwargs.get("pk")
        obj=Category.objects.get(id=id)
        serializer = CategorySerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Category.objects.filter(id=id).delete()
        return Response(data={"message":"category removed"})
    
    @action(methods=["post"],detail=True)
    def add_product(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        category_obj=Category.objects.get(id=id)
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category=category_obj)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class ProductView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def list(self,request,*args,**kwargs):
        qs= Product.objects.all()
        serializer=ProductSerializer(qs, many=True)
        return Response(serializer.data)
    
    def retrieve(self,*args,**kwargs):
        id = kwargs.get("pk")
        qs = Product.objects.get(id=id)
        serializer=ProductSerializer(qs)
        return Response(data=serializer.data)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Product.objects.filter(id=id).delete()
        return Response(data={"message":"product removed"})
    
    def update(self, request,*args,**kwargs):
        id = kwargs.get("pk")
        obj=Product.objects.get(id=id)
        serializer = ProductSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    


        
    
    
    