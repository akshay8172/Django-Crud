from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create,name='create'),
    path('edit/<pk>',views.edit,name='edit'),
    path('delete/<pk>',views.delete,name='delete'),
    path('list/<pk>',views.lists,name='list'),
    path('',views.lists,name='list')
]
