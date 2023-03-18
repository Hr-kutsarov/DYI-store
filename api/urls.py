from django.urls import path
from .views import product_list, product_details
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:id>/', product_details, name='product_details')
]

urlpatterns = format_suffix_patterns(urlpatterns)