from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from base_backend.users.views import AppUserTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('base_backend.users.urls')),
    path('api/token/auth/', AppUserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
