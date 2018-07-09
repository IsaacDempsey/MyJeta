# Generated by Django 2.0.6 on 2018-07-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_stops_operator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coefficients',
            fields=[
                ('segment', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('intercept', models.FloatField(null=True)),
                ('arrivaltime', models.FloatField(null=True)),
                ('rain', models.FloatField(null=True)),
                ('dayofweek_Friday', models.FloatField(null=True)),
                ('dayofweek_Monday', models.FloatField(null=True)),
                ('dayofweek_Saturday', models.FloatField(null=True)),
                ('dayofweek_Sunday', models.FloatField(null=True)),
                ('dayofweek_Thursday', models.FloatField(null=True)),
                ('dayofweek_Tuesday', models.FloatField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Coefficients',
            },
        ),
        migrations.AddIndex(
            model_name='coefficients',
            index=models.Index(fields=['segment'], name='main_coeffi_segment_32dc18_idx'),
        ),
    ]
