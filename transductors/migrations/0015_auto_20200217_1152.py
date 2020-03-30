# Generated by Django 3.0.2 on 2020-02-17 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transductors', '0014_merge_20200217_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energytransductor',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='last_minutely_collection',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='last minutely collection'),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='last_monthly_collection',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='last monthly collection'),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='last_quarterly_collection',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='last quarterly collection'),
        ),
    ]
