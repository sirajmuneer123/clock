from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView

# Create your views here.
class Home1(TemplateView):
    template_name = 'superAdmin/home.html'


class Employee(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'superAdmin/employee.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        ctx = super(Employee, self).get_context_data(**kwargs)
        ctx['value'] = 'Save'
        return ctx

class EmployeeUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'superAdmin/employee.html'
    success_message = "wooow"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        ctx = super(EmployeeUpdate, self).get_context_data(**kwargs)
        ctx['value'] = 'Update'
        return ctx


class EmployeeDelete(DeleteView):
    model = User
    template_name = 'superAdmin/employee.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        ctx = super(EmployeeDelete, self).get_context_data(**kwargs)
        ctx['value'] = 'Confirm'
        ctx['delete'] = True
        return ctx


class Home(ListView):
    template_name = 'superAdmin/home.html'
    paginate_by = 1  # if pagination is desired
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = 'timezone.now()'
        return context

