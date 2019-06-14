from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.conf import settings as SETTINGS
from superAdmin.models import Clock

# Create your views here.
class Home1(TemplateView):
    template_name = 'superAdmin/home.html'


class Employee(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'superAdmin/employee.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        response = super(Employee, self).form_valid(form)
        password = User.objects.make_random_password(length=6)
        self.object.set_password(password)
        grp, created = Group.objects.get_or_create(name="employee")
        self.object.groups.add(grp)
        self.object.save()
        message = "Username : " + self.object.username + ", Password : " + password
        send_password(self.object.email, message)
        return response

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


class ClockDelete(DeleteView):
    model = Clock
    template_name = 'superAdmin/employee.html'
    success_url = reverse_lazy('report')

    def get_context_data(self, **kwargs):
        ctx = super(UpdateDelete, self).get_context_data(**kwargs)
        ctx['value'] = 'Confirm'
        ctx['delete'] = True
        return ctx


class ClockUpdate(UpdateView):
    model = Clock
    fields = ['working_hours', 'breaking_hours', 'meeting_hours']
    template_name = 'superAdmin/employee.html'
    success_message = "wooow"
    success_url = reverse_lazy('report')

    def get_context_data(self, **kwargs):
        ctx = super(ClockUpdate, self).get_context_data(**kwargs)
        ctx['value'] = 'Update'
        return ctx

class Home(ListView):
    template_name = 'superAdmin/home.html'
    paginate_by = 10 
    queryset = User.objects.filter(groups__name="employee")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = 'timezone.now()'
        return context

class ReportView(ListView):
    template_name = 'superAdmin/report.html'
    paginate_by = 10 
    queryset = Clock.objects.all().order_by('-date')


def send_password(to_email, message):
    send_mail(
        'Employee credential',
        message,
        SETTINGS.EMAIL_HOST_USER,
        [to_email],
        fail_silently=False,
    )
    return True
