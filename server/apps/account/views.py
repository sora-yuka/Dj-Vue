from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .serializers import RegisterSerializer

# Create your views here.


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request: Request) -> Response:
        try:
            serializer = RegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response(
                {
                    "MESSAGE": "You signed in successfully!",
                    "STATUS": status.HTTP_201_CREATED
                }, status=status.HTTP_201_CREATED
            )
        except IntegrityError:
            return Response(
                {
                    "MESSAGE": "Something went wrong, please check the output",
                    "STATUS": status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_404_NOT_FOUND
            )