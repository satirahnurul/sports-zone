from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Produk
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
   try:
    product_item = Produk.objects.filter(pk=product_id)
    xml_data = serializers.serialize("xml", product_item)
    return HttpResponse(xml_data, content_type="application/xml")
   except Produk.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try:
    product_item = Produk.objects.get(pk=product_id)
    json_data = serializers.serialize("json", [product_item])
    return HttpResponse(json_data, content_type="application/json")
   except Produk.DoesNotExist:
       return HttpResponse(status=404)
   
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

