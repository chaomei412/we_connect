# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 14:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='previous_login',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 1, 14, 15, 46, 984000, tzinfo=utc)),
        ),
    ]