# Generated by Django 4.1.7 on 2023-03-01 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("bookid", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("booknum", models.IntegerField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("userid", models.IntegerField(primary_key=True, serialize=False)),
                ("password", models.CharField(max_length=128)),
                ("username", models.CharField(max_length=128)),
                ("userlevel", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Record",
            fields=[
                ("rentno", models.IntegerField(primary_key=True, serialize=False)),
                ("borrow_date", models.DateTimeField(auto_now_add=True)),
                ("return_date", models.DateTimeField(blank=True, null=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.book"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.user"
                    ),
                ),
            ],
        ),
    ]
