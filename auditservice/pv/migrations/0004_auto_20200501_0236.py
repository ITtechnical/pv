# Generated by Django 2.2.10 on 2020-05-01 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pv', '0003_auto_20200501_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pv',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pv.Profile'),
        ),
    ]