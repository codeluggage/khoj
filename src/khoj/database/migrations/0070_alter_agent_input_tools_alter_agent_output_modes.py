# Generated by Django 5.0.8 on 2024-10-21 05:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0069_webscraper_serverchatsettings_web_scraper"),
    ]

    operations = []  # type: ignore
    # migrations.AlterField(
    #     model_name="agent",
    #     name="input_tools",
    #     field=django.contrib.postgres.fields.ArrayField(
    #         base_field=models.CharField(
    #             choices=[
    #                 ("general", "General"),
    #                 ("online", "Online"),
    #                 ("notes", "Notes"),
    #                 ("summarize", "Summarize"),
    #                 ("webpage", "Webpage"),
    #             ],
    #             max_length=200,
    #         ),
    #         blank=True,
    #         default=list,
    #         null=True,
    #         size=None,
    #     ),
    # ),
    # migrations.AlterField(
    #     model_name="agent",
    #     name="output_modes",
    #     field=django.contrib.postgres.fields.ArrayField(
    #         base_field=models.CharField(
    #             choices=[("text", "Text"), ("image", "Image"), ("automation", "Automation")], max_length=200
    #         ),
    #         blank=True,
    #         default=list,
    #         null=True,
    #         size=None,
    #     ),
    # ),
