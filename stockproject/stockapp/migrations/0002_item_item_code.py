# Generated by Django 4.1.1 on 2022-11-02 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_code',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
