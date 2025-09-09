from django.shortcuts import render
from .models import Produk
# Create your views here.

def show_main(request):
    context = {
        'npm' : '2406351112',
        'name': 'Satirah Nurul Fikriyyah',
        'class': 'PBP D'
    }
    return render(request,"main.html",context)