# Generated by Django 2.1.5 on 2019-03-07 18:33

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporte', '0004_auto_20190306_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='diario',
            name='act_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actividad_1', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AddField(
            model_name='diario',
            name='act_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actividad_2', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AddField(
            model_name='diario',
            name='act_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actividad_3', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AddField(
            model_name='diario',
            name='act_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actividad_4', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AddField(
            model_name='diario',
            name='act_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actividad_5', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AddField(
            model_name='diario',
            name='act_6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actividad_6', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AddField(
            model_name='diario',
            name='act_7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actividad_7', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AddField(
            model_name='diario',
            name='act_8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actividad_8', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AddField(
            model_name='diario',
            name='act_9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actividad_9', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AddField(
            model_name='diario',
            name='desc_1',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True, verbose_name='Descripcion de la actividad'),
        ),
        migrations.AddField(
            model_name='diario',
            name='desc_2',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True, verbose_name='Descripcion de la actividad'),
        ),
        migrations.AddField(
            model_name='diario',
            name='desc_3',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True, verbose_name='Descripcion de la actividad'),
        ),
        migrations.AddField(
            model_name='diario',
            name='desc_4',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True, verbose_name='Descripcion de la actividad'),
        ),
        migrations.AddField(
            model_name='diario',
            name='desc_5',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True, verbose_name='Descripcion de la actividad'),
        ),
        migrations.AddField(
            model_name='diario',
            name='desc_6',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True, verbose_name='Descripcion de la actividad'),
        ),
        migrations.AddField(
            model_name='diario',
            name='desc_7',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True, verbose_name='Descripcion de la actividad'),
        ),
        migrations.AddField(
            model_name='diario',
            name='desc_8',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True, verbose_name='Descripcion de la actividad'),
        ),
        migrations.AddField(
            model_name='diario',
            name='desc_9',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True, verbose_name='Descripcion de la actividad'),
        ),
        migrations.AddField(
            model_name='diario',
            name='img_1',
            field=models.ImageField(blank=True, null=True, upload_to='reporte', verbose_name='Evidencia'),
        ),
        migrations.AddField(
            model_name='diario',
            name='img_2',
            field=models.ImageField(blank=True, null=True, upload_to='reporte', verbose_name='Evidencia'),
        ),
        migrations.AddField(
            model_name='diario',
            name='img_3',
            field=models.ImageField(blank=True, null=True, upload_to='reporte', verbose_name='Evidencia'),
        ),
        migrations.AddField(
            model_name='diario',
            name='img_4',
            field=models.ImageField(blank=True, null=True, upload_to='reporte', verbose_name='Evidencia'),
        ),
        migrations.AddField(
            model_name='diario',
            name='img_5',
            field=models.ImageField(blank=True, null=True, upload_to='reporte', verbose_name='Evidencia'),
        ),
        migrations.AddField(
            model_name='diario',
            name='img_6',
            field=models.ImageField(blank=True, null=True, upload_to='reporte', verbose_name='Evidencia'),
        ),
        migrations.AddField(
            model_name='diario',
            name='img_7',
            field=models.ImageField(blank=True, null=True, upload_to='reporte', verbose_name='Evidencia'),
        ),
        migrations.AddField(
            model_name='diario',
            name='img_8',
            field=models.ImageField(blank=True, null=True, upload_to='reporte', verbose_name='Evidencia'),
        ),
        migrations.AddField(
            model_name='diario',
            name='img_9',
            field=models.ImageField(blank=True, null=True, upload_to='reporte', verbose_name='Evidencia'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='servicio',
            field=models.CharField(choices=[('Supervision', 'Supervision'), ('Rescate de Flora', 'Rescate de Flora'), ('Rescate de Fauna', 'Resctae de Fauna'), ('Mantenimiento de Flora', 'Mantenimiento de Flora'), ('Monitoreo', 'Monitoreo'), ('Fomento de Seguridad', 'Fomento de Seguridad')], default='SUPERVISION', max_length=20),
        ),
    ]