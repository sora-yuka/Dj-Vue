from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterAPIView


urlpatterns = [
    path("sign_up/", RegisterAPIView.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="obtain_pair_view"),
    path("refresh_token/", TokenRefreshView.as_view(), name="refresh_token"),
]