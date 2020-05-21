from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from market.serializers import AddCategorySerializer,AddProductSerializer,AddCartSerializer


@api_view(['POST'])
def add_category(request):
    serializer = AddCategorySerializer(data=request.data)
    if serializer.is_valid():
        category = serializer.save()
        if category:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_product(request):
    serializer = AddProductSerializer(data=request.data)
    if serializer.is_valid():
        product = serializer.save()
        if product:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_to_cart(request):
    serializer = AddCartSerializer(data=request.data)
    if serializer.is_valid():
        cart = serializer.save()
        if cart:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)