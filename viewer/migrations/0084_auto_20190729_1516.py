# Generated by Django 2.2.3 on 2019-07-29 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0083_auto_20190715_1247'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('scope', 'name')},
        ),
    ]
