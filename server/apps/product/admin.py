from django.contrib import admin
from .models import ProductModel, CategoryModel

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["slug", "category"]


admin.site.register(ProductModel, ProductAdmin)
admin.site.register(CategoryModel)