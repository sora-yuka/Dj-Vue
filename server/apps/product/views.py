from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import ProductModel, CategoryModel
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.


class LatestProductListAPIView(ListAPIView):
    queryset = ProductModel.objects.all()[0:4]
    serializer_class = ProductSerializer
    

class AllProductListAPIView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    

class ProductDetail(APIView):
    def get_object(self, category_slug: str, product_slug: str) -> ProductModel:
        try:
            return ProductModel.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except ProductModel.DoesNotExist:
            raise Http404
    
    def get(self, request: Response, category_slug: str, product_slug: str, format=None) -> Response:
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    

class CategoryDetail(APIView):
    def get_object(self, category_slug: str) -> Response:
        try:
            return CategoryModel.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request: Request, category_slug: str, format=None) -> Response:
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(['POST'])
def search(request: Request) -> Response:
    query = request.data.get('query', '')

    if query:
        products = ProductModel.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})