# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactivechart', '0003_auto_20170331_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default='', max_length=20),
        ),
    ]