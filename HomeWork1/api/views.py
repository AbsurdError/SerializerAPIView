from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
# Create your views here.
class ProductGet(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': serializer.data})


class One(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')
        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response('Product is no exist')
        serializer = ProductSerializer(product)
        return Response({'data': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')
        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response('Product is no exist')
        serializer = ProductSerializer(data=request.data, instance=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': serializer.data})

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')
        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response('Product is no exist')
        serializer = ProductSerializer(data=request.data, instance=product, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')

        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response('Product is no exist')
        product.delete()
        return Response('Product delete')