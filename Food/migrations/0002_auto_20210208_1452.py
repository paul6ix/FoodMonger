# Generated by Django 3.1.6 on 2021-02-08 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='home',
            new_name='model_food',
        ),
        migrations.RenameField(
            model_name='model_food',
            old_name='home_desc',
            new_name='food_desc',
        ),
        migrations.RenameField(
            model_name='model_food',
            old_name='home_name',
            new_name='food_name',
        ),
        migrations.RenameField(
            model_name='model_food',
            old_name='home_price',
            new_name='food_price',
        ),
    ]
