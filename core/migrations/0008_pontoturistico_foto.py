# Generated by Django 2.2.1 on 2019-06-04 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190531_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]
