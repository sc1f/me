# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20170815_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='A description for the category.'),
            preserve_default=False,
        ),
    ]
