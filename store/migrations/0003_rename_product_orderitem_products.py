# Generated by Django 3.2.19 on 2024-03-27 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20240327_1204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='products',
        ),
    ]
