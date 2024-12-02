from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mapa/', views.mapa, name='mapa'),
    path('material/', views.material, name='material'),
    path('proceso/', views.proceso, name='proceso'),
]
