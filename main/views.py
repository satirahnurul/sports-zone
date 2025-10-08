from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Produk
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Produk.objects.all()
    else:
        product_list = Produk.objects.filter(user=request.user)

    context = {
        'npm' : '2406351112',
        'name': request.user.username,
        'class': 'PBP D',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit= False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    produk = get_object_or_404(Produk, pk=id)
    produk.increment_views()

    context = {
        'produk': produk
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Produk.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Produk.objects.all()
    data = [
        {
            'id': str(produk.id),
            'name': produk.name,
            'description': produk.description,
            'category': produk.category,
            'thumbnail': produk.thumbnail,
            'product_views': produk.product_views,
            'created_at': produk.created_at.isoformat() if produk.created_at else None,
            'is_featured': produk.is_featured,
            'user': {
                'id': produk.user.id,
                'username': produk.user.username,
                'email': produk.user.email,
            } if produk.user else None,
        }
        for produk in product_list
    ]

    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
   try:
    product_item = Produk.objects.filter(pk=product_id)
    xml_data = serializers.serialize("xml", product_item)
    return HttpResponse(xml_data, content_type="application/xml")
   except Produk.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try:
        produk = Produk.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(produk.id),
            'name': produk.name,
            'description': produk.description,
            'price': produk.price,
            'stock': produk.stock,
            'category': produk.category,
            'thumbnail': produk.thumbnail,
            'product_views': produk.product_views,
            'created_at': produk.created_at.isoformat() if produk.created_at else None,
            'is_featured': produk.is_featured,
            'user': produk.user.username if produk.user else None,
        }
        return JsonResponse(data)
   except Produk.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    produk = get_object_or_404(Produk, pk=id)
    form = ProductForm(request.POST or None, instance=produk)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    produk = get_object_or_404(Produk, pk=id)
    produk.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
@login_required
def create_product_ajax(request):
    try:
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        thumbnail = request.POST.get('thumbnail')
        category = request.POST.get('category')
        is_featured = request.POST.get('is_featured') == 'on'
        stock = request.POST.get('stock')
        
        if not name or not price or not description:
            return JsonResponse({
                'status': 'error',
                'message': 'Nama, harga, dan deskripsi harus diisi!'
            }, status=400)
        
        product = Produk.objects.create(
            user=request.user,
            name=name,
            price=int(price),
            description=description,
            thumbnail=thumbnail if thumbnail else None,
            category=category if category else 'bola',  
            is_featured=is_featured,
            stock=int(stock) if stock else 0
        )
        
        return JsonResponse({
            'status': 'success',
            'message': 'Product berhasil ditambahkan!',
        }, status=200)
        
    except ValueError as e:
        return JsonResponse({
            'status': 'error',
            'message': 'Format harga atau stock tidak valid!'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Terjadi kesalahan: {str(e)}'
        }, status=400)

@csrf_exempt
@require_POST
@login_required
def edit_product_ajax(request, id):
    try:
        product = Produk.objects.get(id=id, user=request.user)
        
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        thumbnail = request.POST.get('thumbnail')
        category = request.POST.get('category')
        is_featured = request.POST.get('is_featured') == 'on'
        stock = request.POST.get('stock')
        
        if not name or not price or not description:
            return JsonResponse({
                'status': 'error',
                'message': 'Nama, harga, dan deskripsi harus diisi!'
            }, status=400)
        
        product.name = name
        product.price = int(price)
        product.description = description
        product.thumbnail = thumbnail if thumbnail else None
        product.category = category if category else 'bola'
        product.is_featured = is_featured
        product.stock = int(stock) if stock else 0
        product.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Product berhasil diupdate!'
        }, status=200)
        
    except Produk.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Product tidak ditemukan'
        }, status=404)
    except ValueError as e:
        return JsonResponse({
            'status': 'error',
            'message': 'Format harga atau stock tidak valid!'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Terjadi kesalahan: {str(e)}'
        }, status=400)

@csrf_exempt
@require_POST
@login_required
def delete_product_ajax(request, id):
    try:
        product = Produk.objects.get(id=id, user=request.user)
        product.delete()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Product berhasil dihapus!'
        }, status=200)
        
    except Produk.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Product tidak ditemukan'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Terjadi kesalahan: {str(e)}'
        }, status=400)

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if not username or not password1 or not password2:
            return JsonResponse({
                'status': 'error',
                'message': 'Semua field harus diisi!'
            }, status=400)
        
        if password1 != password2:
            return JsonResponse({
                'status': 'error',
                'message': 'Password tidak cocok!'
            }, status=400)
        
        if len(password1) < 8:
            return JsonResponse({
                'status': 'error',
                'message': 'Password minimal 8 karakter!'
            }, status=400)
        
        if request.user.objects.filter(username=username).exists():
            return JsonResponse({
                'status': 'error',
                'message': 'Username sudah digunakan!'
            }, status=400)
        
        try:
            user = request.user.objects.create_user(
                username=username,
                password=password1
            )
            user.save()
            
            return JsonResponse({
                'status': 'success',
                'message': 'Registrasi berhasil! Silakan login.',
                'redirect': reverse('main:login')
            }, status=201)
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Terjadi kesalahan: {str(e)}'
            }, status=400)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=400)

@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({
                'status': 'success',
                'message': 'Login berhasil!',
                'username': user.username,
                'redirect': reverse('main:show_main')
            }, status=200)
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Username atau password salah!'
            }, status=401)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=400)
