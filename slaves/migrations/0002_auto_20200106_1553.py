# Generated by Django 2.1.5 on 2020-01-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subordinates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subordinate',
            name='ip_address',
            field=models.CharField(max_length=50),
        ),
    ]
