# Generated by Django 4.2.7 on 2024-02-09 13:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("realOwner", "0008_brand_remove_category_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="create_profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                (
                    "age",
                    models.PositiveIntegerField(blank=True, max_length=100, null=True),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="bio",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="location",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="profile_picture",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="user",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="email",
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                max_length=1,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="age",
            field=models.PositiveIntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name="edit_user_profile",
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
