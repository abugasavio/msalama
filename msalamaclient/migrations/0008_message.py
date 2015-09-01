# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msalamaclient', '0007_appointment_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('messagefrom', models.CharField(max_length=150)),
                ('messageto', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=800)),
                ('date', models.DateField(auto_now_add=True)),
                ('patient', models.ForeignKey(to='msalamaclient.UserProfile')),
            ],
        ),
    ]
