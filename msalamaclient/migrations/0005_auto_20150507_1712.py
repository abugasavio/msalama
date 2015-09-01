# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('msalamaclient', '0004_vaccinedose_vaccinedoseday'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientvaccination',
            name='dateofvaccinereceiption',
            field=models.DateField(default=datetime.datetime(2015, 5, 7, 17, 12, 19, 187000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientvaccination',
            name='locationofreception',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
