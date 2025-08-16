from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def shop(request):
    return render(request, "shop.html")

def cart(request):
    return render(request, "cart.html")

def login_view(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def otp(request):
    return render(request, "otp.html")

def product(request):
    return render(request, "product.html")

def pay(request):
    return render(request, "pay.html")

def get_mail(request):
    return render(request, "get_mail.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("shop/", shop, name="shop"),
    path("cart/", cart, name="cart"),
    path("login/", login_view, name="login"),
    path("register/", register, name="register"),
    path("otp/", otp, name="otp"),
    path("product/", product, name="product"),
    path("pay/", pay, name="pay"),
    path("get-mail/", get_mail, name="get_mail"),
]
