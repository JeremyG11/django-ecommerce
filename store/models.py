from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225, db_index=True)
    slug = models.SlugField(max_length=225, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='productsproduct_creator', on_delete=models.CASCADE)
    item = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=225)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Product'
        ordering = ('-created',)
    
    
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
        
    def __str__(self):
        return self.item
        
        
        
        
        
        
        
        
        
        
        
        
        