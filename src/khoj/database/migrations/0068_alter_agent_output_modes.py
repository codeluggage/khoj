# Generated by Django 5.0.8 on 2024-10-17 18:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0067_alter_agent_style_icon"),
    ]

    operations = []  # type: ignore
    # migrations.AlterField(
    #     model_name="agent",
    #     name="output_modes",
    #     field=django.contrib.postgres.fields.ArrayField(
    #         base_field=models.CharField(
    #             choices=[("text", "Text"), ("image", "Image"), ("automation", "Automation")], max_length=200
    #         ),
    #         default=list,
    #         size=None,
    #     ),
    # ),
