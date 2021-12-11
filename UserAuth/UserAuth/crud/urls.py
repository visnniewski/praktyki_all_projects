from django.urls import path
from . import views

app_name = 'crud'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:note_id>/', views.noteview, name="noteview"),
    path('<int:note_id>/edit/', views.edit, name="edit"),
    path('add/', views.add, name="add"),
    path('addnote/', views.addnote, name="addnote"),
]