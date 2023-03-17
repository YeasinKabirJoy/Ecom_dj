import uuid
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    slug = models.SlugField(default="", blank=True, null=False, max_length=1000)

    class Meta:
        ordering = ['name']

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self) :
        return self.name
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,unique=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    slug = models.SlugField(default="", blank=True, null=False, max_length=1000)

    class Meta:
        ordering = ['name']

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self) :
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(SubCategory,on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    slug = models.SlugField(default="", blank=True, null=False, max_length=1000)

    class Meta:
        ordering = ['created']

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self) :
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productImage/')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)