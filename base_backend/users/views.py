from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView

from base_backend.users.serializers import AppUserTokenObtainPairSerializer


class AppUserTokenObtainPairView(TokenObtainPairView):
    serializer_class = AppUserTokenObtainPairSerializer
