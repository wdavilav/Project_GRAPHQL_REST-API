from django.urls import path

from core.api.views import ProductListAPIView, ProductListByCategoryAPIView

urlpatterns = [
    path('product/', ProductListAPIView.as_view(), name='api_product_list'),
    path('product/<int:pk>/', ProductListAPIView.as_view(), name='api_product_list'),
    path('product/by/category/<str:category>/', ProductListByCategoryAPIView.as_view(), name='api_product_by_category'),
]
