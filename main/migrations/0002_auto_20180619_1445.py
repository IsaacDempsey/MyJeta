# Generated by Django 2.0.6 on 2018-06-19 13:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dublinbusstops',
            name='operator',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='dublinbusstops',
            name='routes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None),
        ),
    ]
