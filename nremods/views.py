from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Register
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created successfully!")
        return redirect("login")

    return render(request, "register.html")


# Login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials!")
            return redirect("login")

    return render(request, "login.html")


# Logout
def logout_view(request):
    logout(request)
    return redirect("home")
def home(request):
    return render(request, "home.html")

def shop(request):
    return render(request, "shop.html")

def cart(request):
    return render(request, "cart.html")

def otp(request):
    return render(request, "otp.html")

def product(request):
    return render(request, "product.html")

def pay(request):
    return render(request, "pay.html")

def get_mail(request):
    return render(request, "get_mail.html")
