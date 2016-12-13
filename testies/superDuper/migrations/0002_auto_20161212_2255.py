# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-12 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superDuper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icao', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('latitude_deg', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude_deg', models.DecimalField(decimal_places=6, max_digits=9)),
                ('elevation_ft', models.IntegerField()),
                ('continent', models.CharField(max_length=200)),
                ('iso_country', models.CharField(max_length=200)),
                ('iso_common_name', models.CharField(max_length=200)),
                ('iso_region', models.CharField(max_length=200)),
                ('municipality', models.CharField(max_length=200)),
                ('gps_code', models.CharField(max_length=200)),
                ('iata_code', models.CharField(max_length=200)),
                ('local_code', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]