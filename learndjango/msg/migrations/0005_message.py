# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('msg', '0004_delete_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=400)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
