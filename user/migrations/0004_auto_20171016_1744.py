# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 17:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20171001_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('can_view_users', 'Can view users awaiting checkup for registration.'),)},
        ),
    ]
