# Generated by Django 5.1.6 on 2025-05-20 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("interview_result", "0003_alter_interviewresultqas_question"),
    ]

    operations = [
        migrations.AlterField(
            model_name="interviewresultqas",
            name="question",
            field=models.TextField(),
        ),
    ]
