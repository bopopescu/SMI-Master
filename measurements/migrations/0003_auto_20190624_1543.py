# Generated by Django 2.1.5 on 2019-06-24 18:43

import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0002_auto_20190506_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlymeasurement',
            name='active_max_power_list_off_peak_time',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(), default=None, size=None),
        ),
        migrations.AlterField(
            model_name='monthlymeasurement',
            name='active_max_power_list_peak_time',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(), default=None, size=None),
        ),
        migrations.AlterField(
            model_name='monthlymeasurement',
            name='reactive_max_power_list_off_peak_time',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(), default=None, size=None),
        ),
        migrations.AlterField(
            model_name='monthlymeasurement',
            name='reactive_max_power_list_peak_time',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(), default=None, size=None),
        ),
    ]