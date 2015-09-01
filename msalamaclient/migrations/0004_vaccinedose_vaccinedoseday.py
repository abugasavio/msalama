# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('msalamaclient', '0003_auto_20150507_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccinedose',
            name='vaccinedoseday',
            field=models.DateField(default=datetime.datetime(2015, 5, 7, 9, 55, 38, 776124)),
            preserve_default=False,
        ),
    ]
