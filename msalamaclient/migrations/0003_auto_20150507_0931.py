# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msalamaclient', '0002_auto_20150507_0850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaccine',
            old_name='VaccineDoseCount',
            new_name='vaccineDoseCount',
        ),
        migrations.RenameField(
            model_name='vaccine',
            old_name='VaccineEdition',
            new_name='vaccineEdition',
        ),
        migrations.RenameField(
            model_name='vaccine',
            old_name='VaccineIDnum',
            new_name='vaccineIDnum',
        ),
        migrations.RenameField(
            model_name='vaccine',
            old_name='Vaccinename',
            new_name='vaccinename',
        ),
        migrations.RemoveField(
            model_name='vaccinedose',
            name='vaccinedoseday',
        ),
    ]
