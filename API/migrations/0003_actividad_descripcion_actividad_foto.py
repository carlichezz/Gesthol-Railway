# Generated by Django 5.0.6 on 2024-07-01 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_reserva_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='descripcion',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='actividad',
            name='foto',
            field=models.CharField(default='2', max_length=500),
        ),
    ]
