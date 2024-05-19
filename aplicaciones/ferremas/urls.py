from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos),
    path('agregarproducto/', views.agregarproducto)
]