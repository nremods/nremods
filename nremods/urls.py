from django.contrib import admin
from django.urls import path
from nremods import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("cart/", views.cart, name="cart"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("otp/", views.otp, name="otp"),
    path("product/", views.product, name="product"),
    path("pay/", views.pay, name="pay"),
    path("get-mail/", views.get_mail, name="get_mail"),
]
