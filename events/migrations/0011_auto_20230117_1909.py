# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2023-01-17 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20180206_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_cropping',
            field=image_cropping.fields.ImageRatioField('event_picture', '800x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='Beskjæring'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_picture',
            field=models.ImageField(blank=True, help_text='Bilder som er større enn 800x300 px ser best ut. Du kan beskjære bildet etter opplasting.', null=True, upload_to='uploads/event_pictures', verbose_name='Arrangementbilde'),
        ),
    ]
