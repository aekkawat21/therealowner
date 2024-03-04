# Generated by Django 4.2.7 on 2024-03-04 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("realOwner", "0023_alter_phonecategory_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phonecategory",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="realOwner.category"
            ),
        ),
    ]
