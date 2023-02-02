# Generated by Django 2.0.2 on 2018-03-01 10:58

from django.db import migrations, models
import django.db.models.deletion
import i18nfield.fields
import pretalx.common.mixins.models


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0010_event_plugins"),
        ("person", "0013_auto_20180122_1615"),
    ]

    operations = [
        migrations.CreateModel(
            name="SpeakerInformation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("include_submitters", models.BooleanField(default=False)),
                ("exclude_unconfirmed", models.BooleanField(default=False)),
                ("title", i18nfield.fields.I18nCharField(max_length=200)),
                ("text", i18nfield.fields.I18nTextField()),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="information",
                        to="event.Event",
                    ),
                ),
            ],
            bases=(pretalx.common.mixins.models.LogMixin, models.Model),
        ),
    ]
