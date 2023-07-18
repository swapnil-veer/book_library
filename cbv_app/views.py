# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from http import HTTPStatus


class CbvView(View):  
    def get(self, request):
        print("in get method")  
        return HttpResponse('response')  

    def post(self, request):
        data = request.POST
        nm =data.get("name")
        age = data.get("age")

        print("in post request")
        return HttpResponse("in post method", status = HTTPStatus.CREATED)   #201- resource created
    
from .models import Employee  
from .forms import EmployeeForm  
from django.views.generic.edit import CreateView  
  
class EmployeeCreate(CreateView):  
    model = Employee  
    fields = '__all__'  
    success_url = 'http://127.0.0.1:8000/cbv/emp-create'
    

from django.views.generic.list import ListView
class EmployeeList(ListView):   #object_list
    model = Employee
    context_object_name = "all_employee"
    # if you do not want to iterate with object_list then you must add "context_object_name = " in class as a veraible

from django.views.generic.detail import DetailView
class EmployeeDetailView(DetailView):
    model = Employee


from django.views.generic.edit import UpdateView
 
class EmployeeUpdateView(UpdateView):
    # specify the model you want to use
    model = Employee
    fields = '__all__'
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = 'http://127.0.0.1:8000/cbv/emp-list'

from django.views.generic.edit import DeleteView
 
class EmployeeDeleteView(DeleteView):
    # specify the model you want to use
    model = Employee
   
    success_url = 'http://127.0.0.1:8000/cbv/emp-list'