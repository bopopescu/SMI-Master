# Generated by Django 3.0.2 on 2020-01-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20200129_1635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consumptionabovecontract',
            options={'verbose_name': 'consumption above contracted threshold'},
        ),
        migrations.AlterModelOptions(
            name='consumptionpeakevent',
            options={'verbose_name': 'consumption peak'},
        ),
        migrations.AlterModelOptions(
            name='criticalvoltageevent',
            options={'verbose_name': 'critical voltage'},
        ),
        migrations.AlterModelOptions(
            name='failedconnectionsubordinateevent',
            options={'verbose_name': 'failed connection with subordinate server'},
        ),
        migrations.AlterModelOptions(
            name='failedconnectiontransductorevent',
            options={'verbose_name': 'failed connection with meter'},
        ),
        migrations.AlterModelOptions(
            name='phasedropevent',
            options={'verbose_name': 'phase drop'},
        ),
        migrations.AlterModelOptions(
            name='precariousvoltageevent',
            options={'verbose_name': 'precarious voltage'},
        ),
        migrations.AlterModelOptions(
            name='voltagerelatedevent',
            options={'verbose_name': 'voltage related'},
        ),
        migrations.AlterField(
            model_name='consumptionrelatedevent',
            name='consumption',
            field=models.FloatField(default=0.0, verbose_name='consumption related'),
        ),
    ]
