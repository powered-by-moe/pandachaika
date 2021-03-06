# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import viewer.models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0023_archive_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='thumbnail',
            field=models.ImageField(default='', max_length=500, upload_to=viewer.models.gallery_thumb_path_handler),
        ),
        migrations.AddField(
            model_name='gallery',
            name='thumbnail_url',
            field=models.URLField(blank=True, default='', max_length=10, null=True),
        ),
    ]
