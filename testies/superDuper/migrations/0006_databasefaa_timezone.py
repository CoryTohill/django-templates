# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-16 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superDuper', '0005_auto_20161215_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='databasefaa',
            name='timezone',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
