from django.urls import path
from . import views


urlpatterns = [

    path('', views.welcome_page ),
    path('form/', views.form_view ),    
    path('products', views.view_products),
    path('products/delete/<str:id>/', views.delete_product),
    path('products/edit/<str:id>/', views.edit_product),
    path('products/view/<str:id>/', views.view_product),
    path('categories/add/', views.create_category),
    ]