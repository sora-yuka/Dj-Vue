from io import BytesIO
from PIL import Image

from django.db import models
from django.contrib.auth import get_user_model
from django.core.files import File

# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField()
    
    class Meta:
        ordering = ["name"]
        
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return f"/{self.slug}/"
    

class ProductModel(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    thumbnail = models.ImageField(upload_to="uploads/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        CategoryModel, 
        related_name="products",
        on_delete=models.CASCADE, 
        )
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self) -> str:
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self) -> str:
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self) -> str:
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail