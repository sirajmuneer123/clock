from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.conf import settings as SETTINGS
from superAdmin.models import Clock
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.l


class Employee(LoginRequiredMixin, CreateView):
    """ To create emoloyee
    """
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
        message = "EmployeeId : " + self.object.username + ", Password : " + password
        send_password(self.object.email, message)
        return response

    def get_context_data(self, **kwargs):
        ctx = super(Employee, self).get_context_data(**kwargs)
        ctx['value'] = 'Save'
        ctx['navigation'] = 'Employee'
        return ctx

class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    """ To update emolyee details
    """
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'superAdmin/employee.html'
    success_message = "wooow"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        ctx = super(EmployeeUpdate, self).get_context_data(**kwargs)
        ctx['value'] = 'Update'
        return ctx


class EmployeeDelete(LoginRequiredMixin, DeleteView):
    """ To delete Employee
    """
    model = User
    template_name = 'superAdmin/employee.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        ctx = super(EmployeeDelete, self).get_context_data(**kwargs)
        ctx['value'] = 'Confirm'
        ctx['delete'] = True
        return ctx


class ClockDelete(LoginRequiredMixin, DeleteView):
    """ To delete clock one day entry
    """
    model = Clock
    template_name = 'superAdmin/employee.html'
    success_url = reverse_lazy('report')

    def get_context_data(self, **kwargs):
        ctx = super(ClockDelete, self).get_context_data(**kwargs)
        ctx['value'] = 'Confirm'
        ctx['delete'] = True
        return ctx


class ClockUpdate(LoginRequiredMixin, UpdateView):
    """ To update clock one day details
    """
    model = Clock
    fields = ['working_hours', 'breaking_hours', 'meeting_hours']
    template_name = 'superAdmin/employee.html'
    success_message = "wooow"
    success_url = reverse_lazy('report')

    def get_context_data(self, **kwargs):
        ctx = super(ClockUpdate, self).get_context_data(**kwargs)
        ctx['value'] = 'Update'
        return ctx

class Home(LoginRequiredMixin, ListView):
    """ To list all employees
    """
    template_name = 'superAdmin/home.html'
    paginate_by = 10 
    queryset = User.objects.filter(groups__name="employee").order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = 'timezone.now()'
        return context

class ReportView(LoginRequiredMixin, ListView):
    """ To list clock details of all employees
    """
    template_name = 'superAdmin/report.html'
    paginate_by = 10
    queryset = Clock.objects.all().order_by('-date')


def send_password(to_email, message):
    """ To send mail
    """
    send_mail(
        'Employee credential',
        message,
        SETTINGS.EMAIL_HOST_USER,
        [to_email],
        fail_silently=False,
    )
    return True

