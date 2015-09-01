# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msalamaclient', '0008_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='messagesubject',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
