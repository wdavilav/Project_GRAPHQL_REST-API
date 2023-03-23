from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from core.api.serializers import ProductSerializers
from core.store.models import Product


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [AllowAny]


class ProductListByIdAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [AllowAny]

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return self.queryset.filter(id=self.kwargs['pk'])
        return self.queryset.all()


class ProductListByCategoryAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [AllowAny]

    def get_queryset(self):
        category = self.kwargs['category']
        return self.queryset.filter(category__name__icontains=category)
