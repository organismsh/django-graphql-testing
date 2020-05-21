from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    discount = models.DecimalField(decimal_places=2, max_digits=10)


class Products(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.DecimalField(decimal_places=2, max_digits=10,default=0)
    product_type =models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductImages(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/products/products')

class ProductThumbnailImages(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/products/thumbnail')


class Cart(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE,related_name="cart_product")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    