# Generated by Django 5.1 on 2024-08-23 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_remove_livro_autor_remove_livro_coautor_and_more"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="capa",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
