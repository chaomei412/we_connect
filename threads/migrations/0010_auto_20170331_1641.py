# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 15:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0009_auto_20170331_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 31, 15, 41, 9, 835000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 31, 15, 41, 9, 835000, tzinfo=utc)),
        ),
    ]
