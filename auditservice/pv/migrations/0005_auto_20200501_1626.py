# Generated by Django 2.2.10 on 2020-05-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pv', '0004_auto_20200501_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_director',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_management',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_standard',
            field=models.BooleanField(default=False),
        ),
    ]
