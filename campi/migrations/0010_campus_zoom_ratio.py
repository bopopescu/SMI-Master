# Generated by Django 3.0.2 on 2020-03-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campi', '0009_auto_20200320_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='zoom_ratio',
            field=models.DecimalField(decimal_places=0, default=14, max_digits=2, verbose_name='map zoom'),
        ),
    ]
