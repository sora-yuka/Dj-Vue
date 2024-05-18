from django.urls import path
from .views import (
    LatestProductListAPIView,
    AllProductListAPIView,
    # ProductDetailedAPIView,
    ProductDetail,
    CategoryDetail,
    search,
    )

urlpatterns = [
    path("latest/", LatestProductListAPIView.as_view()),
    path("all/", AllProductListAPIView.as_view()),
    path("<slug:category_slug>/<slug:product_slug>/", ProductDetail.as_view()),
    path("<slug:category_slug>/", CategoryDetail.as_view()),
    path("search/", search),
]