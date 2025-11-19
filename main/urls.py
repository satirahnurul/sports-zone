from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product, register_ajax, login_ajax, create_product_ajax, edit_product_ajax, delete_product_ajax, proxy_image, create_products_flutter, show_my_products_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-produk/', create_product, name='create_product'),
    path('produk/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('produk/<uuid:id>/edit', edit_product, name='edit_product'),
    path('produk/<uuid:id>/delete', delete_product, name='delete_product'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('create-product-ajax/', create_product_ajax, name='create_product_ajax'),
    path('edit-product-ajax/<uuid:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<uuid:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_products_flutter, name='create_products_flutter'),
    path('json/my-products/', show_my_products_json, name='show_my_products_json'),
]