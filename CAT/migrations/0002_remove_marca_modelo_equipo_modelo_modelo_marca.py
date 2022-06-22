# Generated by Django 4.0.5 on 2022-06-21 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CAT', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marca',
            name='modelo',
        ),
        migrations.AddField(
            model_name='equipo',
            name='modelo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CAT.modelo'),
        ),
        migrations.AddField(
            model_name='modelo',
            name='marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CAT.marca'),
        ),
    ]