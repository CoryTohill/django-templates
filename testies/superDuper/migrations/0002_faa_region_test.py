# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-15 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superDuper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faa_region',
            name='test',
            field=models.CharField(default='asdf', max_length=300),
            preserve_default=False,
        ),
    ]
