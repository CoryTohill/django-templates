# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-12 23:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superDuper', '0002_auto_20161212_2255'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Airport',
            new_name='AirportsFiltered',
        ),
    ]
