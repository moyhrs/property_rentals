# Generated by Django 4.2.11 on 2024-03-06 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_property"),
    ]

    operations = [
        migrations.CreateModel(
            name="PropertyTenant",
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
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("deposit_amount", models.IntegerField()),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.property"
                    ),
                ),
                (
                    "tenant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.tenant"
                    ),
                ),
            ],
            options={
                "db_table": "properties_tenants",
            },
        ),
        migrations.AddConstraint(
            model_name="propertytenant",
            constraint=models.UniqueConstraint(
                fields=("property", "tenant"), name="unique_property_tenant"
            ),
        ),
    ]