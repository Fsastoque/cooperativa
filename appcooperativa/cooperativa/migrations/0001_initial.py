# Generated by Django 2.2.15 on 2022-09-11 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('documento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=20)),
                ('ceclular', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Lineas_De_Credito',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_linea', models.CharField(max_length=30)),
                ('plazo_maximo', models.IntegerField()),
                ('monto_maximo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='credito',
            fields=[
                ('codigo_credito', models.IntegerField(primary_key=True, serialize=False)),
                ('monto_prestado', models.IntegerField()),
                ('fecha', models.DateField()),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperativa.Lineas_De_Credito')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperativa.cliente')),
            ],
        ),
    ]
