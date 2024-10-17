from django.urls import path
from .views import getRoutes,CreateUserView,UserDetails

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',getRoutes),
    path('user/register/', CreateUserView, name='register'),
    path('user/details/', UserDetails, name='user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]