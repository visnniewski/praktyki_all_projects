
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('book_rent.urls')),
    path('admin/', admin.site.urls),
]
