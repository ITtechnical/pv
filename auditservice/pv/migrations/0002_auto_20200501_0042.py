# Generated by Django 2.2.10 on 2020-05-01 00:42

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pv',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pv',
            name='modified',
            field=models.DateTimeField(null=True, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date.today)]),
        ),
        migrations.AddField(
            model_name='pv',
            name='modified_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified', to=settings.AUTH_USER_MODEL),
        ),
    ]
