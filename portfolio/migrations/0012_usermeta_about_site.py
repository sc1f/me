# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20170815_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermeta',
            name='about_site',
            field=models.TextField(default='About this site', verbose_name='About Site'),
            preserve_default=False,
        ),
    ]
