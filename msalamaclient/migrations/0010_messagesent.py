# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msalamaclient', '0009_message_messagesubject'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageSent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=800)),
                ('messagesubject', models.CharField(max_length=100, blank=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('patient', models.ForeignKey(to='msalamaclient.UserProfile')),
            ],
        ),
    ]
