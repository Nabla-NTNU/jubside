# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-10 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_eventregistration_checked_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='check_in_time',
            field=models.DateTimeField(blank=True, help_text='Hvis sjekket inn: tidspunkt for innsjekk.', null=True, verbose_name='Innsjekkstidspunkt'),
        ),
    ]
