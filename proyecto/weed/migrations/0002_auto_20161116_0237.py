# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-16 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weed',
            name='latitud',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='weed',
            name='longitud',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
