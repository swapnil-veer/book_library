"""
URL configuration for Book_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from cbv_app.views import CbvView, EmployeeCreate, EmployeeList,EmployeeDetailView, EmployeeUpdateView, EmployeeDeleteView

urlpatterns = [
    path('view/', CbvView.as_view(), name = 'cb_view'),
     path('emp-create', EmployeeCreate.as_view(), name = 'EmployeeCreate'), 
     path('emp-list', EmployeeList.as_view(), name = 'Employeelist'), 
     path('emp-detail/<pk>/', EmployeeDetailView.as_view(), name = 'Employeedetail'), 
     path('emp-update/<pk>/', EmployeeUpdateView.as_view(), name = 'Employee_update'), 
     path('emp-delete/<pk>/', EmployeeDeleteView.as_view(), name = 'Employee_delete'), 



]