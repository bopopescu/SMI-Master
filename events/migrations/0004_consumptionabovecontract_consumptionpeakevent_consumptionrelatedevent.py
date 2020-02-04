# Generated by Django 2.1.5 on 2020-01-15 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20200115_0154'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumptionRelatedEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
                ('consumption', models.FloatField(default=0.0)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='ConsumptionAboveContract',
            fields=[
                ('consumptionrelatedevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.ConsumptionRelatedEvent')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('events.consumptionrelatedevent',),
        ),
        migrations.CreateModel(
            name='ConsumptionPeakEvent',
            fields=[
                ('consumptionrelatedevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.ConsumptionRelatedEvent')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('events.consumptionrelatedevent',),
        ),
    ]