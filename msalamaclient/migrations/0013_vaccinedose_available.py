# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msalamaclient', '0012_auto_20150812_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccinedose',
            name='available',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
