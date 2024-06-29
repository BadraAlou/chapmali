from django.urls import path
from chapmaliApp import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('order/<int:product_id>/', views.order_product, name='order_product'),
    path('order/<int:order_id>/confirmation/', views.order_confirmation, name='order_confirmation'),
    path('about/', views.about, name='about'),
    path('submit_suggestion/', views.submit_suggestion, name='submit_suggestion'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('order_confirmation_authenticated/', views.order_confirmation_authenticated, name='order_confirmation_authenticated'),
    path('accounts/', include('django.contrib.auth.urls')),  # Inclure les URLs d'authentification de Django
     path('order/<int:order_id>/download_invoice/', views.download_invoice, name='download_invoice'),
]
