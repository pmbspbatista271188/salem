# Generated by Django 2.2.10 on 2020-02-27 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0004_carrusel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrusel',
            name='img',
            field=models.ImageField(upload_to='imagenes/carrusel/'),
        ),
    ]