# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0006_auto_20160412_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendmail',
            name='password',
        ),
    ]
