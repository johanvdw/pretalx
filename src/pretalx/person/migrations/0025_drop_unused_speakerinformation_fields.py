# Generated by Django 3.1.4 on 2021-01-30 22:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("person", "0024_date_migration_information_target_group"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="speakerinformation",
            name="exclude_unconfirmed",
        ),
        migrations.RemoveField(
            model_name="speakerinformation",
            name="include_submitters",
        ),
    ]
