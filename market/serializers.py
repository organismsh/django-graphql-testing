from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from market.models import Category,Products,Cart

class AddCategorySerializer(serializers.Serializer):
    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Category.objects.all())]
    )

    discount = serializers.DecimalField(
        required=True,
        decimal_places = 2,
        max_digits=10
    )
   

    def validate(self, validated_data):
        
        return validated_data
    
    def create(self, validated_data):
        category = Category.objects.create(
            **validated_data
        )
        return validated_data

class AddProductSerializer(serializers.Serializer):
    product_name = serializers.CharField(
        required=True
    )

    description = serializers.CharField(
        required=True
    )

    price = serializers.DecimalField(
        required=True,
        decimal_places = 2,
        max_digits=10
    )

    product_type = serializers.IntegerField(
        required=True
    )
    
    

    def validate(self, validated_data):
        if not Category.objects.filter(id=validated_data["product_type"]).exists():
            raise serializers.ValidationError({"response":"category_not_found"})
        return validated_data
    
    def create(self, validated_data):
        product_type = Category.objects.get(id=validated_data["product_type"])

        category = Products.objects.create(
            product_name = validated_data['product_name'],
            description = validated_data["description"],
            price = validated_data["price"],
            product_type = product_type
        )
        return validated_data


class AddCartSerializer(serializers.Serializer):
    product = serializers.IntegerField(
        required=True
    )


    def validate(self, validated_data):
        
        if not Products.objects.filter(id=validated_data["product"]).exists():
            raise serializers.ValidationError({"response":"invalid_product_id"})

        if Cart.objects.filter(product__id=validated_data["product"]).exists():
            raise serializers.ValidationError({"response":"product_exists"})


        return validated_data
    
    def create(self, validated_data):
        product = Products.objects.get(id=validated_data["product"])
        cart = Cart.objects.create(
            product = product
        )
        return validated_data