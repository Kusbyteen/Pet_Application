# Generated by Django 4.2.3 on 2023-07-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adoptions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
