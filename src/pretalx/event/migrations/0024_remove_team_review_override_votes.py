# Generated by Django 3.1 on 2020-09-24 21:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0023_update_featured_visibility"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="team",
            name="review_override_votes",
        ),
    ]
