# Generated by Django 4.2.11 on 2024-03-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_landlord_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tenant",
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
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("phone_number", models.CharField(max_length=20, null=True)),
            ],
            options={
                "db_table": "tenants",
            },
        ),
    ]