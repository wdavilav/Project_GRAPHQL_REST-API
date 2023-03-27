import graphene
from graphene_django import DjangoObjectType

from .models import Product, Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('id', 'name', 'code', 'category', 'price', 'stock')


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_products(root, info):
        return Product.objects.all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
