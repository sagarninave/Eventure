# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-22 05:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180921_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='gallery',
        ),
        migrations.DeleteModel(
            name='image',
        ),
    ]
