# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 22:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0040_auto_20170727_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archive',
            old_name='matchtype',
            new_name='match_type',
        ),
    ]
