# Generated by Django 3.0 on 2021-02-13 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentMethod',
        ),
    ]
