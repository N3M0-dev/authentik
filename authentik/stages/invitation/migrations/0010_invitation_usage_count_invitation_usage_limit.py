# Generated by Django 5.0.13 on 2025-03-27 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_stages_invitation", "0009_invitation_authentik_s_expires_96f4b8_idx_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="invitation",
            name="usage_count",
            field=models.PositiveIntegerField(
                default=0, help_text="How many times this invitation has been used."
            ),
        ),
        migrations.AddField(
            model_name="invitation",
            name="usage_limit",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Maximum number of times this invitation can be used. 0 means unlimited.",
            ),
        ),
    ]
