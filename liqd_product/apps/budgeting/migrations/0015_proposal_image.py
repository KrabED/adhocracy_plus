# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-21 08:10
from __future__ import unicode_literals

import adhocracy4.images.fields
from django.db import migrations


class Migration(migrations.Migration):

    replaces = [('meinberlin_budgeting', '0015_proposal_image')]

    dependencies = [
        ('liqd_product_budgeting', '0014_proposal_is_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='image',
            field=adhocracy4.images.fields.ConfiguredImageField('idea_image', blank=True, upload_to='ideas/images'),
        ),
    ]
