# Generated by Django 2.1.2 on 2018-12-11 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veggie',
            name='breakfast_food',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='veggie',
            name='dinner_food',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='veggie',
            name='lunch_food',
            field=models.BooleanField(default=False),
        ),
    ]