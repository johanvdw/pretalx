# Generated by Django 1.11.4 on 2017-08-20 17:16

from django.db import migrations


def strip_submission_codes(apps, schema_editor):
    Submission = apps.get_model("submission", "Submission")

    for pk in Submission.objects.all().values_list("pk", flat=True):
        submission = Submission.objects.get(pk=pk)
        submission.code = submission.code.strip()
        submission.save()


class Migration(migrations.Migration):
    dependencies = [
        ("submission", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(strip_submission_codes, migrations.RunPython.noop),
    ]
