# Generated by Django 4.1 on 2022-09-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Worked",
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
                ("position", models.CharField(max_length=200)),
                ("company", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=50)),
                ("start_date", models.CharField(max_length=100)),
                ("end_date", models.CharField(max_length=100)),
            ],
        ),
    ]
