# Generated by Django 4.0.4 on 2022-05-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listGames', '0002_rename_rates_currency_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='rate',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
