# Generated by Django 4.1.5 on 2023-02-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0006_alter_measurement_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='picture',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
