# Generated by Django 4.2.7 on 2024-03-04 06:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("realOwner", "0025_delete_phonecategory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="brand",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
