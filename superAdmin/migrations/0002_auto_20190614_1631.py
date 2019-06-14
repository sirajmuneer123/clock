# Generated by Django 2.2.2 on 2019-06-14 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superAdmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clock',
            name='updated',
        ),
        migrations.AlterField(
            model_name='clock',
            name='breaking_hours',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='clock',
            name='meeting_hours',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='clock',
            name='status',
            field=models.CharField(choices=[('0', 'Stop'), ('1', 'Workig'), ('2', 'Break'), ('3', 'Meeting')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='clock',
            name='working_hours',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]