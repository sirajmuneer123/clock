from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('employee', views.Employee.as_view(), name='employee'),
    path('employee-update/<int:pk>/', views.EmployeeUpdate.as_view(), name='employee-update'),
    path('employee-delete/<int:pk>/', views.EmployeeDelete.as_view(), name='employee-delete'),
    path('report/', views.ReportView.as_view(), name='report'),
    path('clock-update/<int:pk>/', views.ClockUpdate.as_view(), name='clock-update'),
    path('clock-delete/<int:pk>/', views.ClockDelete.as_view(), name='clock-delete'),
]