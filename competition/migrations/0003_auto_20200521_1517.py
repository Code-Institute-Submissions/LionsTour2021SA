# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-21 15:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0002_auto_20200514_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='submit_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
