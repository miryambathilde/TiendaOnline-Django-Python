# Generated by Django 2.2.3 on 2021-04-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_auto_20210412_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='Dirección de envío'),
        ),
    ]