# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 20:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0011_auto_20170330_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 30, 20, 16, 9, 413000, tzinfo=utc)),
        ),
    ]
