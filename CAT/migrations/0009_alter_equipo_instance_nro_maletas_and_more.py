# Generated by Django 4.0.5 on 2022-06-22 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAT', '0008_alter_certificado_fecha_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo_instance',
            name='nro_maletas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='manual',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]