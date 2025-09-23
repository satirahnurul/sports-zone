from django.forms import ModelForm
from main.models import Produk

class ProductForm(ModelForm):
    class Meta:
        model = Produk
        fields = ["name", "price", "description", "category", "thumbnail", "is_featured", "stock"]

