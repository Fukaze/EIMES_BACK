# Generated by Django 4.0.5 on 2022-06-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAT', '0004_alter_equipo_instance_certif_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo_instance',
            name='nro_maletas',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='equipo_instance',
            name='proveedor',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
