# Generated by Django 5.0.6 on 2024-07-01 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_actividad_descripcion_actividad_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='descripcion',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='foto',
            field=models.CharField(default='', max_length=500),
        ),
    ]
