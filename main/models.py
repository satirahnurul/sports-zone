from django.db import models

# Create your models here.

class Produk(models.Model):
    CATEGORY = [
        ('sepatu bola', 'Sepatu Bola'),
        ('kaos kaki', 'Kaos Kaki'),
        ('jersey', 'Jersey'),
        ('tas bola', 'Tas Bola'),
        ('bola', 'Bola'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY, default='ball')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
