# Generated by Django 4.0.3 on 2024-09-24 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_checkout_checkoutproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutproducts',
            name='pid',
            field=models.IntegerField(default=None),
        ),
    ]
