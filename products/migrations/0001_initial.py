# Generated by Django 5.1.2 on 2024-10-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="Price"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "changed",
                    models.DateTimeField(auto_now=True, verbose_name="Changed"),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]
