from django.urls import path
from . import views

app_name = "book_rent"
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
]
