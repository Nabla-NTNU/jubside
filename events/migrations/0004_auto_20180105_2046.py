# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-05 20:46
from __future__ import unicode_literals

from django.db import migrations
import uuid

def gen_uuid(apps, schema_editor):
    Eventregistration = apps.get_model('events', 'Eventregistration')
    for row in Eventregistration.objects.all():
        row.ticket_id = uuid.uuid4()
        row.save(update_fields=['ticket_id'])

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventregistration_ticket_id'),
    ]


    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
