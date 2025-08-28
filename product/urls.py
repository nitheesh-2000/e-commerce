from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('home', views.menu,name='home'),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('store/', views.store, name="store"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('', views.account, name="login"),
	path('blank_layout/', views.blank_layout, name="blank_layout"),
	path('product_details/<int:pk>', views.product_details, name="product_details"),
	path('products/', views.products, name="products"),
	path('product_list', views.products_list, name="list_product"),
	path('product_description/', views.product_description, name="product_description"),


]

 