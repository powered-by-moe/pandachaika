# Generated by Django 2.2 on 2019-04-18 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0076_auto_20190417_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archive',
            options={'permissions': (('publish_archive', 'Can publish available archives'), ('match_archive', 'Can match archives'), ('update_metadata', 'Can update metadata'), ('upload_with_metadata_archive', 'Can upload a file with an associated metadata source'))},
        ),
    ]