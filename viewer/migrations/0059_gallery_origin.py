# Generated by Django 2.1 on 2018-08-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0058_auto_20180807_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='origin',
            field=models.SmallIntegerField(choices=[(1, 'Normal'), (2, 'Submitted')], db_index=True, default=1),
        ),
    ]