# Generated by Django 3.0 on 2021-01-23 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_auto_20210123_1407'),
        ('Payment', '0003_deliverymethod'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DeliveryMethod',
        ),
    ]