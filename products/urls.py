from django.urls import path

from . import views

urlpatterns = [
    path('products', views.products, name='products'),
    path('user/98/addproducts' , views.addproducts, name='addproducts'),
    path('user/98/addproducts/edit/<id>', views.editproduct, name='editproduct'),
    path('product/<str:title>/',views.viewproduct , name='viewproduct'),
]