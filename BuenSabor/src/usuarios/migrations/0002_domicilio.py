# Generated by Django 3.2.4 on 2021-06-18 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=100, verbose_name='Teléfono')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('localidad', models.CharField(max_length=100, verbose_name='Teléfono')),
            ],
        ),
    ]
