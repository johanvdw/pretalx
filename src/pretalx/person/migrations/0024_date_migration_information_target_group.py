# Generated by Django 3.1.4 on 2021-01-30 22:23

from django.db import migrations


def update_target_group(apps, schema_editor):
    """We start showing proposals in all states in the public featured list.

    That's something of a backwards-incompatible state, so we make sure
    that no previously-invisible proposal becomes visible.
    """

    SpeakerInformation = apps.get_model("person", "SpeakerInformation")
    logic = {
        (True, True): "accepted",  # should never occur, resort to default value
        (True, False): "submitters",
        (False, True): "confirmed",
        (False, False): "accepted",
    }
    for information in SpeakerInformation.objects.all():
        information.target_group = logic[
            (information.include_submitters, information.exclude_unconfirmed)
        ]
        information.save()


class Migration(migrations.Migration):
    dependencies = [
        ("person", "0023_speakerinformation_target_group"),
    ]

    operations = [migrations.RunPython(update_target_group, migrations.RunPython.noop)]
