# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msalamaclient', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientvaccination',
            old_name='Patient',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='sideeffect',
            old_name='Patient',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='sideeffect',
            old_name='Vaccine',
            new_name='vaccine',
        ),
        migrations.RenameField(
            model_name='vaccinedose',
            old_name='Vaccine',
            new_name='vaccine',
        ),
        migrations.RenameField(
            model_name='vaccinedose',
            old_name='Vaccinedose',
            new_name='vaccinedose',
        ),
        migrations.AlterField(
            model_name='patientvaccination',
            name='vaccinedose',
            field=models.ForeignKey(to='msalamaclient.VaccineDose'),
        ),
    ]
