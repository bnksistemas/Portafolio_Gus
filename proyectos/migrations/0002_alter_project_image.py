# Generated by Django 5.0.3 on 2024-04-01 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='proyectos', verbose_name='Imagen'),
        ),
    ]
