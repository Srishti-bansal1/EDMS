# Generated by Django 4.2.9 on 2024-01-28 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("EDMSapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Emp_address",
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
                (
                    "Address",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="EDMSapp.edmsmodel",
                    ),
                ),
            ],
        ),
    ]
