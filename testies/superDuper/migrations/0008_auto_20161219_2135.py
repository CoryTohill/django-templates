# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-19 21:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superDuper', '0007_auto_20161219_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='databasefaatimezone',
            old_name='city_id',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='databasefaatimezone',
            old_name='timezone_id',
            new_name='timezone',
        ),
    ]
