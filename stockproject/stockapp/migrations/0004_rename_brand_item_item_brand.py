# Generated by Django 4.1.1 on 2022-11-04 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0003_alter_item_item_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='brand',
            new_name='item_brand',
        ),
    ]
