# Generated by Django 3.0.2 on 2020-01-29 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transductors', '0005_auto_20200129_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energytransductor',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 15, 5, 46, 581574), verbose_name='created at'),
        ),
    ]