# Generated by Django 5.1.4 on 2025-04-16 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.CharField(max_length=32)),
            ],
            options={
                "db_table": "account",
            },
        ),
        migrations.CreateModel(
            name="AccountRoleType",
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
                (
                    "roleType",
                    models.CharField(
                        choices=[("ADMIN", "Admin"), ("NORMAL", "Normal")],
                        default="NORMAL",
                        max_length=64,
                    ),
                ),
            ],
            options={
                "db_table": "account_role_type",
            },
        ),
        migrations.CreateModel(
            name="WithdrawalMembership",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("accountId", models.CharField(max_length=50)),
                ("withdraw_at", models.DateTimeField(null=True)),
                ("withdraw_end", models.DateTimeField(null=True)),
            ],
            options={
                "db_table": "withdrawal_membership",
            },
        ),
    ]
