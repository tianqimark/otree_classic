# Generated by Django 2.2.12 on 2021-06-11 08:15

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('even_gamble_practice', '0010_auto_20210611_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='cq1_4',
            field=otree.db.models.PositiveIntegerField(choices=[[1, 'Pressing the Up Arrow key (↑); wwwww w www w w wwwwww w www wwwww w www w wwww w ww'], [2, 'Pressing the Down Arrow key (↓)']], null=True),
        ),
    ]