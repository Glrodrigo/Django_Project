# Generated by Django 4.1.1 on 2022-09-24 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dia_semanaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Dia_semana')),
                ('day', models.IntegerField(verbose_name='Data')),
                ('month', models.IntegerField(verbose_name='Mes')),
            ],
        ),
    ]
