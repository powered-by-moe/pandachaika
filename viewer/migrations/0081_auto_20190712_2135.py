# Generated by Django 2.2.3 on 2019-07-13 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0080_auto_20190711_1912'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archive',
            options={'permissions': (('publish_archive', 'Can publish available archives'), ('manage_archive', 'Can manage available archives'), ('match_archive', 'Can match archives'), ('update_metadata', 'Can update metadata'), ('upload_with_metadata_archive', 'Can upload a file with an associated metadata source'))},
        ),
    ]