# Generated by Django 2.2.12 on 2021-06-11 08:04

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('even_gamble_practice', '0007_auto_20210611_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='cq1_4',
            field=otree.db.models.PositiveIntegerField(choices=[[1, 'To accept: Pressing the Up Arrow key (↑)'], [2, 'To reject: Pressing the Down Arrow key (↓)']], null=True),
        ),
    ]