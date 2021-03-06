# Generated by Django 3.0 on 2020-10-11 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=50)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("uuid", models.UUIDField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Film",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("director", models.CharField(max_length=100)),
                ("producer", models.CharField(max_length=100)),
                ("release_date", models.IntegerField()),
                ("rt_score", models.IntegerField()),
                ("modified", models.DateTimeField(auto_now=True)),
                ("uuid", models.UUIDField(null=True, unique=True)),
                (
                    "people",
                    models.ManyToManyField(related_name="films", to="movielist.Person"),
                ),
            ],
        ),
    ]
