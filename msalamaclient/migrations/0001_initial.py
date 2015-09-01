# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientVaccination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vaccinationdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sideeffect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complaint', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateofbirth', models.DateField()),
                ('height', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('IDNum', models.CharField(max_length=200)),
                ('Residence', models.CharField(max_length=200)),
                ('PhoneNum', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Vaccinename', models.CharField(max_length=200)),
                ('VaccineIDnum', models.CharField(max_length=150)),
                ('VaccineEdition', models.CharField(max_length=150)),
                ('Lastupdate', models.DateField()),
                ('VaccineDoseCount', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='vaccinedose',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Vaccinedose', models.CharField(max_length=150)),
                ('vaccinedoseday', models.CharField(max_length=50)),
                ('Vaccine', models.ForeignKey(to='msalamaclient.Vaccine')),
            ],
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='Patient',
            field=models.ForeignKey(to='msalamaclient.UserProfile'),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='Vaccine',
            field=models.ForeignKey(to='msalamaclient.Vaccine'),
        ),
        migrations.AddField(
            model_name='patientvaccination',
            name='Patient',
            field=models.ForeignKey(to='msalamaclient.UserProfile'),
        ),
        migrations.AddField(
            model_name='patientvaccination',
            name='patient_vaccine',
            field=models.ForeignKey(to='msalamaclient.Vaccine'),
        ),
        migrations.AddField(
            model_name='patientvaccination',
            name='vaccinedose',
            field=models.ForeignKey(to='msalamaclient.vaccinedose'),
        ),
    ]
