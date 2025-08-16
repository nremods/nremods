from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from nremods import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("shop/", shop, name="shop"),
    path("cart/", cart, name="cart"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("otp/", otp, name="otp"),
    path("product/", product, name="product"),
    path("pay/", pay, name="pay"),
    path("get-mail/", get_mail, name="get_mail"),
]


