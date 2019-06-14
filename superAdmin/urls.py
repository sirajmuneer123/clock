from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('employee', views.Employee.as_view(), name='employee'),
    path('employee-update/<int:pk>/', views.EmployeeUpdate.as_view(), name='employee-update'),
    path('employee-delete/<int:pk>/', views.EmployeeDelete.as_view(), name='employee-delete'),
]