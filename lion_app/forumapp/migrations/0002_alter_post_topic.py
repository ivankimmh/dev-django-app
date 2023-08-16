# Generated by Django 4.2.3 on 2023-08-11 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("forumapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="topic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="forumapp.topic",
            ),
        ),
    ]
