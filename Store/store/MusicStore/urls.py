from django.urls import path

from . import views

app_name = 'MusicStore'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<int:album_id>/', views.detail, name='detail'),
    path('<int:album_id>/edit', views.edit, name='edit'),
    path('<int:album_id>/editsave', views.editsave, name='editsave'),
]