from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("🚀 Hello, Django is running on Render!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home), 
]
