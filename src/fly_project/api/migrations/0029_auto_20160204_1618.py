# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20160204_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizsubmission',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course'),
        ),
    ]
