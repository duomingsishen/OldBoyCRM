# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 02:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_auto_20151227_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='valid_end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 26, 2, 55, 21, 883726, tzinfo=utc)),
        ),
        migrations.AlterUniqueTogether(
            name='studyrecord',
            unique_together=set([('course_record', 'student')]),
        ),
    ]
