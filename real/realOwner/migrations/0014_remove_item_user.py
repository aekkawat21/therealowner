# Generated by Django 4.2.7 on 2024-02-14 20:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("realOwner", "0013_item_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="user",
        ),
    ]
