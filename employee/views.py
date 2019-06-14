from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from datetime import datetime, timedelta, date
from superAdmin.models import Clock
from django.views import View
from django.http import HttpResponse
import json
# Create your views here.
class Home(TemplateView):
    template_name = 'employee/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clock_obj'] = Clock.objects.get(date=date.today())
        return context

class startView(View):
    """ To start clock
    """
    def post(self, request, *args, **kwargs):
        data = self.request.POST
        type_value = data.get('type', False)
        date = datetime.now()
        try:
            obj = Clock.objects.get(date=date.today())
            old_type = obj.status
            if obj.status == '1':
                start = obj.work_start
                diff = date - start
                obj.working_hours = obj.working_hours + diff
                obj.status = type_value
            elif obj.status == '2':
                start = obj.break_start
                diff = date - start
                obj.breaking_hours = obj.breaking_hours + diff
                obj.status = type_value
            elif obj.status == '3':
                start = obj.meeting_start
                diff = date - start
                obj.meeting_hours = obj.meeting_hours + diff
                obj.status = type_value
            elif obj.status == '0':
                if type_value == '1':
                    obj.work_start = datetime.now()
                elif type_value == '3':
                    obj.break_start = datetime.now()
                elif type_value == '1':
                    obj.meeting_start = datetime.now()
                obj.status = type_value
                obj.save()
            if type_value == '1':
                obj.work_start = datetime.now()
            elif type_value == '2':
                obj.break_start = datetime.now()
            elif type_value == '3':
                obj.meeting_start = datetime.now()
            obj.save()
            return HttpResponse(json.dumps({'status': "1", "old_type": old_type}))
        except Exception as e:
            return HttpResponse(json.dumps({'status': "0", 'error': str(e)}))



class stopView(View):
    """ To start clock
    """
    def post(self, request, *args, **kwargs):
        data = self.request.POST
        type_value = data.get('type', False)
        date = datetime.now()
        obj = Clock.objects.get(date=date.today())
        old_type = obj.status
        try:
            if obj.status == '1':
                start = obj.work_start
                diff = date - start
                obj.working_hours = obj.working_hours + diff
                obj.status = "0"
            elif obj.status == '2':
                start = obj.break_start
                diff = date - start
                obj.breaking_hours = obj.breaking_hours + diff
                obj.status = "0"
            elif obj.status == '3':
                start = obj.meeting_start
                diff = date - start
                obj.meeting_hours = obj.meeting_hours + diff
                obj.status = "0"
            obj.save()
            return HttpResponse(json.dumps({"status": "1", "old_type": old_type}))
        except Exception as e:
            return HttpResponse(json.dumps({"status": "0", 'error': str(e)}))



class IdleView(View):
    """ To start clock
    """
    def post(self, request, *args, **kwargs):
        data = self.request.POST
        status = data.get('status', False)
        date_now = datetime.now()
        date = datetime.now() - timedelta(minutes=10)
        obj = Clock.objects.get(date=date.today())
        old_type = obj.status
        try:
            if old_type == "1":
                if status == 'start':
                    obj.break_start = date
                elif status == 'stop':
                    start = obj.break_start
                    diff = date_now - start
                    obj.breaking_hours = obj.breaking_hours + diff
                obj.save()
            return HttpResponse(json.dumps({"status": "1"}))
        except Exception as e:
            return HttpResponse(json.dumps({"status": "0", 'error': str(e)}))

