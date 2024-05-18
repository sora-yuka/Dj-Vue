from typing import Dict
from rest_framework import serializers
from .models import ProductModel, CategoryModel


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductModel
        fields = [
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            "category"
        ]


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoryModel
        fields = [
            "id",
            "name",
            "get_absolute_url",
            "products"
        ]
    
    def to_representation(self, instance: CategoryModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        products = ProductModel.objects.filter(category=instance.id)
        representation["products"] = ProductSerializer(products, many=True).data
        return representation