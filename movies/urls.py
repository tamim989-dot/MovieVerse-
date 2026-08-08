from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:id>/', views.detail, name='detail'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('privacy/', views.privacy, name='privacy'),
path('disclaimer/', views.disclaimer, name='disclaimer'),
]
