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

    custom_field = graphene.String()

    def resolve_custom_field(self, info):
        return "hello!"


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType, id=graphene.Int())
    all_products_by_category = graphene.List(ProductType, category=graphene.String(required=True))
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_products(root, info, id=None):
        if id is None:
            return Product.objects.all()
        return Product.objects.filter(pk=id)

    def resolve_all_products_by_category(root, info, category):
        if len(category):
            return Product.objects.filter(category__name__icontains=category)
        return Product.objects.all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
