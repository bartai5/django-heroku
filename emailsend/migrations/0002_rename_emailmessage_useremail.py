# Generated by Django 5.0.3 on 2024-03-09 21:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("emailsend", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="EmailMessage",
            new_name="UserEmail",
        ),
    ]
