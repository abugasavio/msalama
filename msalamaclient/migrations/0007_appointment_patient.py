# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msalamaclient', '0006_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(default=24683728, to='msalamaclient.UserProfile'),
            preserve_default=False,
        ),
    ]
