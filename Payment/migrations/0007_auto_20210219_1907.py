# Generated by Django 3.0 on 2021-02-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0006_auto_20210215_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverymethod',
            name='cost',
            field=models.FloatField(default=0.0),
        ),
    ]
