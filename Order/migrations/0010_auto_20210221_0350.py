# Generated by Django 3.0 on 2021-02-21 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0009_auto_20210221_0043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created']},
        ),
    ]