# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-16 17:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 11, 16, 17, 33, 41, 362468, tzinfo=utc)),
            preserve_default=False,
        ),
    ]