from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.

class Clock(models.Model):
    status = (
        ('0', 'Stop'),
        ('1', 'Workig'),
        ('2', 'Break'),
        ('3', 'Meeting'),
    )
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=status, default='1')
    working_hours = models.DurationField(default=timedelta())
    breaking_hours = models.DurationField(default=timedelta())
    meeting_hours = models.DurationField(default=timedelta())
    work_start = models.DateTimeField(blank=True, null=True)
    break_start = models.DateTimeField(blank=True, null=True)
    meeting_start = models.DateTimeField(blank=True, null=True)
    date = models.DateField()
    # updated = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()

    def __str__(self):
        return self.employee.first_name
