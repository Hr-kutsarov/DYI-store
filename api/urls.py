from django.urls import path
from .views import ProductList, ProductDetail, StoreList, StoreDetail, SectionList, SectionDetail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_details'),
    path('store/', SectionList.as_view(), name='product_list'),
    path('store/<int:pk>/', SectionDetail.as_view(), name='product_details'),
    path('section/', StoreList.as_view(), name='product_list'),
    path('section/<int:pk>/', StoreDetail.as_view(), name='product_details')
]

urlpatterns = format_suffix_patterns(urlpatterns)
