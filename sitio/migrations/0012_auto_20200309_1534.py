# Generated by Django 2.2.10 on 2020-03-09 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0011_auto_20200309_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modopago',
            options={'ordering': ['nombre'], 'verbose_name': 'ModoPago', 'verbose_name_plural': 'ModoPagos'},
        ),
    ]
