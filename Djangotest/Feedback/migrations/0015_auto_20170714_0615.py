# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 00:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0014_auto_20170714_0609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbackcommentlog',
            old_name='feedback_weightING',
            new_name='feedback_weighting',
        ),
    ]
