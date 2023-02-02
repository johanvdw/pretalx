# Generated by Django 3.1.4 on 2021-01-30 22:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("submission", "0055_unset_is_featured_flag"),
        ("person", "0021_auto_20200124_1213"),
    ]

    operations = [
        migrations.AddField(
            model_name="speakerinformation",
            name="limit_tracks",
            field=models.ManyToManyField(to="submission.Track"),
        ),
        migrations.AddField(
            model_name="speakerinformation",
            name="limit_types",
            field=models.ManyToManyField(to="submission.SubmissionType"),
        ),
    ]
