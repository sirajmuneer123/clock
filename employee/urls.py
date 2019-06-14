from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='employee-home'),
    path('start/', views.startView.as_view(), name='start'),
    path('stop/', views.stopView.as_view(), name='stop'),
    path('idle-time/', views.IdleView.as_view(), name='idle-time'),
]