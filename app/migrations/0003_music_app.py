# Generated by Django 3.2.12 on 2022-04-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app", "0002_delete_tracks"),
    ]

    operations = [
        migrations.CreateModel(
            name="music_app",
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
                ("trackName", models.CharField(max_length=20)),
                ("artistName", models.CharField(max_length=70)),
                ("exp_id", models.IntegerField()),
            ],
        ),
    ]