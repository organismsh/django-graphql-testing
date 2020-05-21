from graphene_django import DjangoObjectType
import graphene
from .models import Products,ProductImages,Cart

class Product(DjangoObjectType):
    class Meta:
        model = Products

class Carts(DjangoObjectType):
    class Meta:
        model = Cart



class Query(graphene.ObjectType):
    products = graphene.List(Product)
    cart = graphene.List(Carts)
    product = graphene.Field(Product, product_id=graphene.String())

    def resolve_products(self, info):
        return Products.objects.all()
    
    def resolve_cart(self, info):
        return Cart.objects.all()

    def resolve_product(self, info, product_id):
        return Products.objects.get(pk=product_id)
 
    
schema = graphene.Schema(query=Query)