# Generated by Django 2.2.6 on 2019-12-20 03:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='items',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None),
        ),
    ]
