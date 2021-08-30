
from django.contrib import admin
from django.urls import path
from website import views 

urlpatterns = [
    path("",views.index,name="website"),
    path("login/",views.login,name="login"),
    path("cart/",views.cart,name="cart"),
]
