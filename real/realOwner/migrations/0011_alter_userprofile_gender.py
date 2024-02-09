# Generated by Django 4.2.7 on 2024-02-09 19:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("realOwner", "0010_delete_create_profile_userprofile_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "ชาย"), ("F", "หญิง"), ("O", "อื่น")],
                max_length=1,
                null=True,
            ),
        ),
    ]
