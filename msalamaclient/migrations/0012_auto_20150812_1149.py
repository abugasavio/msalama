# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msalamaclient', '0011_auto_20150508_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientvaccination',
            old_name='vaccinationdate',
            new_name='creationdate',
        ),
    ]
