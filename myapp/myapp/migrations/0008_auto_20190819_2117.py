# Generated by Django 2.2.4 on 2019-08-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20190819_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myshop',
            name='image',
            field=models.ImageField(upload_to='Изображения'),
        ),
    ]
