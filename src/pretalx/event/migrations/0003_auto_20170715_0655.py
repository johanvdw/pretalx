# Generated by Django 1.11.3 on 2017-07-15 11:55

import datetime as dt
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0002_auto_20170429_1018"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="date_from",
            field=models.DateField(default=dt.date(2017, 7, 15)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="event",
            name="date_to",
            field=models.DateField(default=dt.date(2017, 7, 15)),
            preserve_default=False,
        ),
    ]
