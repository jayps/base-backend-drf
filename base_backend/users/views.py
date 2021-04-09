from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from base_backend.users.models import AppUser
from base_backend.users.serializers import (
    AppUserTokenObtainPairSerializer,
    RegisterSerializer,
    UserSerializer,
)


class AppUserTokenObtainPairView(TokenObtainPairView):
    serializer_class = AppUserTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            created_user = AppUser.objects.create(
                first_name=serializer.validated_data.get("first_name"),
                last_name=serializer.validated_data.get("last_name"),
                email=serializer.validated_data.get("email"),
            )
            created_user.set_password(serializer.validated_data.get("password"))
            created_user.save()
        except IntegrityError:
            return Response(
                data="The email address you've selected is already in use.",
                status=status.HTTP_400_BAD_REQUEST,
            )

        result = UserSerializer(created_user)
        return Response(data=result.data, status=status.HTTP_201_CREATED)
