# Generated by Django 4.0.3 on 2024-09-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Done')], default=0)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
