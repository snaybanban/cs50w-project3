# Generated by Django 3.0.7 on 2021-06-01 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210527_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Iniciada', 'Iniciada'), ('Terminada', 'Terminada'), ('Reintegrada', 'Reintegrada')], default='Iniciada', max_length=64),
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
    ]
