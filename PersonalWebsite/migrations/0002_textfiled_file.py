# Generated by Django 5.1.2 on 2025-01-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PersonalWebsite", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="textfiled",
            name="file",
            field=models.FileField(
                blank=True, null=True, upload_to="static/text_files/"
            ),
        ),
    ]
