# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-03 03:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]