# Generated by Django 4.0.4 on 2022-06-12 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listGames', '0004_alter_currency_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='store',
            field=models.TextField(blank=True),
        ),
    ]
