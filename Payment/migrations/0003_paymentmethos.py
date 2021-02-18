# Generated by Django 3.0 on 2021-02-13 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0002_delete_paymentmethod'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('PAYPAL', 'PayPal'), ('CARD', 'Card'), ('COD', 'Cash On Delivary')], max_length=10)),
                ('description', models.TextField()),
            ],
        ),
    ]