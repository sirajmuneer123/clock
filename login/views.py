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
                print ("Group : ", user_group)
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
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)



class RegisterView(FormView):
    """
    Provides the ability to register as a user with a username and password
    """
    form_class = AuthenticationForm
    template_name = "common/register.html"

    def post(self, request):
        username = self.request.POST['username']
        password = self.request.POST['password']
        return HttpResponseRedirect('/register')