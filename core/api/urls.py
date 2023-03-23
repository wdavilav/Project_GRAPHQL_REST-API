from django.urls import path

from core.api.views import *

urlpatterns = [
    path('product/', ProductListAPIView.as_view(), name='api_product_list'),
    path('product/<int:id>/', ProductListByIdAPIView.as_view(), name='api_product_list_id'),
    path('product/category/<str:category>/', ProductListByCategoryAPIView.as_view(), name='api_product_by_category'),
]
