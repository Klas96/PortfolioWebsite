# Generated by Django 5.1.4 on 2025-01-28 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalWebsite', '0004_alter_artproject_id_alter_audiofile_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Certificate',
        ),
        migrations.DeleteModel(
            name='PersonalDescription',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
    ]
