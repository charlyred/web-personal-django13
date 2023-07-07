# Generated by Django 4.2.2 on 2023-07-04 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("porfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={
                "ordering": ["-created"],
                "verbose_name": "proyecto",
                "verbose_name_plural": "proyectos",
            },
        ),
        migrations.AddField(
            model_name="project",
            name="link",
            field=models.URLField(blank=True, null=True, verbose_name="Sitio web"),
        ),
        migrations.AlterField(
            model_name="project",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Fecha de creación"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(verbose_name="Descripción"),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="projects", verbose_name="Imagen"),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Título"),
        ),
        migrations.AlterField(
            model_name="project",
            name="updated",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Fecha de modificación"
            ),
        ),
    ]
