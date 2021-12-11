from django.urls import path, include
from . import views

app_name = 'User'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('<str:username>/', include('crud.urls')),
]