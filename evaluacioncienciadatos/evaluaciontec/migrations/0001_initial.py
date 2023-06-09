# Generated by Django 4.1.7 on 2023-03-03 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carrera',
            fields=[
                ('idCarrera', models.AutoField(db_column='idCarrera', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='nombre', max_length=50, null=True)),
            ],
            options={
                'db_table': 'carrera',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDepartamento', models.IntegerField(blank=True, db_column='idDepartamento', null=True)),
                ('nombre', models.CharField(blank=True, db_column='nombre', max_length=60, null=True)),
            ],
            options={
                'db_table': 'departamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='evaluaciondepartamento',
            fields=[
                ('idEvaluacion', models.AutoField(db_column='idEvaluacion', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='nombre', max_length=60, null=True)),
                ('promedio', models.DecimalField(db_column='promedio', decimal_places=2, max_digits=10)),
                ('numeroAlumnos', models.IntegerField(blank=True, db_column='numeroAlumnos', null=True)),
                ('aspectos', models.CharField(blank=True, db_column='aspectos', max_length=60, null=True)),
                ('puntaje', models.DecimalField(db_column='puntaje', decimal_places=2, max_digits=10)),
                ('calificacion', models.CharField(blank=True, db_column='calificacion', max_length=30, null=True)),
                ('year', models.IntegerField(blank=True, db_column='year', null=True)),
                ('semestre', models.CharField(blank=True, db_column='semestre', max_length=40, null=True)),
            ],
            options={
                'db_table': 'evaluaciondepartamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='evaluacionmaestro',
            fields=[
                ('idEvaluacion', models.AutoField(db_column='idEvaluacion', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='nombre', max_length=60, null=True)),
                ('promedio', models.DecimalField(db_column='promedio', decimal_places=2, max_digits=10)),
                ('numeroAlumnos', models.IntegerField(blank=True, db_column='numeroAlumnos', null=True)),
                ('aspectos', models.CharField(blank=True, db_column='aspectos', max_length=60, null=True)),
                ('puntaje', models.DecimalField(db_column='puntaje', decimal_places=2, max_digits=10)),
                ('calificacion', models.CharField(blank=True, db_column='calificacion', max_length=30, null=True)),
                ('year', models.IntegerField(blank=True, db_column='year', null=True)),
                ('semestre', models.CharField(blank=True, db_column='semestre', max_length=40, null=True)),
            ],
            options={
                'db_table': 'evaluacionmaestro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='maestros',
            fields=[
                ('idMaestro', models.AutoField(db_column='idMaestro', primary_key=True, serialize=False)),
                ('plantel', models.CharField(blank=True, db_column='plantel', max_length=60, null=True)),
                ('rfc', models.CharField(blank=True, db_column='rfc', max_length=13, null=True)),
                ('curp', models.CharField(blank=True, db_column='curp', max_length=19, null=True)),
                ('apellidoPaterno', models.CharField(blank=True, db_column='apellidoPaterno', max_length=20, null=True)),
                ('apellidoMaterno', models.CharField(blank=True, db_column='apellidoMaterno', max_length=20, null=True)),
                ('nombre', models.CharField(blank=True, db_column='nombre', max_length=30, null=True)),
                ('email', models.CharField(blank=True, db_column='email', max_length=40, null=True)),
            ],
            options={
                'db_table': 'maestros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idU', models.AutoField(db_column='idU', primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, db_column='email', max_length=30, null=True)),
                ('nombres', models.CharField(blank=True, db_column='nombres', max_length=20, null=True)),
                ('apellidos', models.CharField(blank=True, db_column='apellidos', max_length=20, null=True)),
            ],
            options={
                'db_table': 'usuarios',
                'managed': False,
            },
        ),
    ]
