from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='register'),
    path('sign_in/', views.sign_in, name='login'),
    path('sign_out/', views.sign_out, name='logout'),
    path('create/', views.create, name='create'),
    path('view/<int:pk>/', views.view, name='view'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('db/', views.db, name='db'),

    #path('customer/<str:pk>', views.customer, name="customer"),
]
