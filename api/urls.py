from django.urls import path
from .views import ProductList, ProductDetail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_details')
]

urlpatterns = format_suffix_patterns(urlpatterns)
