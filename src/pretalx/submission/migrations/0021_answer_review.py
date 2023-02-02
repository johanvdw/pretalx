# Generated by Django 2.0.2 on 2018-02-06 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("submission", "0020_submission_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="review",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="answers",
                to="submission.Review",
            ),
        ),
    ]
