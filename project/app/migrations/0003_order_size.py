# Generated by Django 3.0.7 on 2020-08-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.CharField(default='DEFAULT VALUE', max_length=100),
        ),
    ]
