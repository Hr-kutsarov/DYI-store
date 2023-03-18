from django.urls import path
from . views import RegisterApiView, LoginApiView, LogoutApiView
urlpatterns = [
    path('register/', RegisterApiView.as_view(), name ='api_register'),
    path('login/', LoginApiView.as_view(), name='api_login'),
    path('logout/', LogoutApiView.as_view(), name='api_logout')
]