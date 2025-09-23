import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Produk(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    CATEGORY = [
        ('sepatu bola', 'Sepatu Bola'),
        ('kaos kaki', 'Kaos Kaki'),
        ('jersey', 'Jersey'),
        ('tas bola', 'Tas Bola'),
        ('bola', 'Bola'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY, default='ball')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    @property
    def is_product_hot(self):
        return self.product_views > 10
        
    def increment_views(self):
        self.product_views += 1
        self.save()

    def add_stock(self, quantity):
        self.stock += quantity
        self.save()
    


    
