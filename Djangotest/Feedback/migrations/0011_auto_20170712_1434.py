# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0010_auto_20170518_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursefeedbackassignment',
            name='feedback_weighting',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='coursefeedbackassignment',
            name='is_given',
            field=models.IntegerField(default=0),
        ),
    ]