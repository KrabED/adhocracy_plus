# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meinberlin_mapideas', '0008_help_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapidea',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Title'),
        ),
    ]
