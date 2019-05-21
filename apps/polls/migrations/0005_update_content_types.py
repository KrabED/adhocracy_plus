# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-27 15:13
from __future__ import unicode_literals

from django.db import migrations

sql = """UPDATE django_content_type
         SET app_label = 'liqd_product_polls'
         WHERE app_label = 'meinberlin_polls';"""

reverse_sql = """UPDATE django_content_type
                 SET app_label = 'meinberlin_polls';
                 WHERE app_label = 'liqd_product_polls';"""


class Migration(migrations.Migration):

    replaces = [('liqd_product_polls', '0005_update_content_types')]

    dependencies = [
        ('a4_candy_polls', '0004_question_multiple_choice'),
    ]

    operations = [
        migrations.RunSQL(sql, reverse_sql)
    ]
