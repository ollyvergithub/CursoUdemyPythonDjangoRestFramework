# Generated by Django 2.2.1 on 2019-05-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
