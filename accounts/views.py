from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import RoleChoices


class UserRegister(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        role = request.data.pop('role', None)
        role = RoleChoices.GENERAL
        request.data['role'] = role
        serializer =  UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)