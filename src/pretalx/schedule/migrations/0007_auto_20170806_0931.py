# Generated by Django 1.11.4 on 2017-08-06 14:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0006_talkslot_is_visible"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="schedule",
            options={"ordering": ("-published",)},
        ),
    ]
