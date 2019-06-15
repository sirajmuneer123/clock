from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView, RedirectView
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout, authenticate
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.contrib import messages
from superAdmin.models import Clock
from datetime import datetime, timedelta, date
from django.contrib.auth.models import User , Group
# Create your views here.
class LoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    form_class = AuthenticationForm
    template_name = "common/webLogin.html"

    def post(self, request):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                user_group = str(user.groups.all()[0])
                if user_group == 'superadmin':
                    return HttpResponseRedirect('/superadmin/')
                elif user_group == 'employee':
                    obj, created = Clock.objects.update_or_create(
                        employee=request.user,
                        date=date.today(),
                        defaults={
                            'work_start': datetime.now(),
                            'status': '1'
                        })
                    return HttpResponseRedirect('/employee/')
                else:
                    return HttpResponseRedirect('/')
            else:
                messages.error(self.request,
                               _("User is not Active"))
                return HttpResponseRedirect('/')
        else:
            messages.error(self.request,
                           _("User Does not Exist"))
            return HttpResponseRedirect(settings.LOGIN_URL)



class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/'

    def get(self, request, *args, **kwargs):

        if self.request.user.groups.filter(name="employee").exists():
            date = datetime.now()
            obj = Clock.objects.get(employee=request.user, date=date.today())
            old_type = obj.status
            if obj.status == '1':
                start = obj.work_start
                diff = date - start
                obj.working_hours = obj.working_hours + diff
            elif obj.status == '2':
                start = obj.break_start
                diff = date - start
                obj.breaking_hours = obj.breaking_hours + diff
            elif obj.status == '3':
                start = obj.meeting_start
                diff = date - start
                obj.meeting_hours = obj.meeting_hours + diff
            obj.save()
            auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)



class RegisterView(FormView):
    """
    Provides the ability to register as a user with some details
    """
    form_class = AuthenticationForm
    template_name = "common/register.html"

    def post(self, request):
        try:
            data = self.request.POST
            password = data.get('password', '')
            repeat_password = data.get('repeatPassword', '')
            username = data.get('username', '')
            if password != repeat_password:
                messages.error(self.request, _("Password Mismatch!"))
                return HttpResponseRedirect('/register')
            if User.objects.filter(username=username).exists():
                messages.error(self.request, _("Username already exist!"))
                return HttpResponseRedirect('/register')
            user = User.objects.create(
                username=username,
                first_name=data.get('first_name', ''),
                last_name=data.get('last_name', ''),
                email=data.get('email', ''),
            )
            user.set_password(password)
            user.save()
            grp, created = Group.objects.get_or_create(name="superadmin")
            user.groups.add(grp)
            return HttpResponseRedirect('/')
        except Exception as e:
            return HttpResponseRedirect('/register')
