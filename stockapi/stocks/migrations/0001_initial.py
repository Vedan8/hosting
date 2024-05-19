# Generated by Django 5.0.6 on 2024-05-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StockData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("symbol", models.CharField(max_length=10)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("avg_returns", models.FloatField()),
                ("avg_close", models.FloatField()),
                ("data", models.JSONField()),
            ],
        ),
    ]
