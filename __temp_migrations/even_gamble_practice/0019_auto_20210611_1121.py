# Generated by Django 2.2.12 on 2021-06-11 10:21

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('even_gamble_practice', '0018_auto_20210611_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='cq2_1',
            field=otree.db.models.PositiveIntegerField(choices=[[1, '40 points'], [2, '25 points']], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='cq2_2',
            field=otree.db.models.PositiveIntegerField(choices=[[1, '40 points'], [2, '25 points']], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='cq2_3',
            field=otree.db.models.PositiveIntegerField(choices=[[1, 'Wining: 25 percent; Losing: 75 percent'], [2, 'Wining: 40 percent; Losing: 60 percent'], [3, 'Wining: 50 percent; Losing: 50 percent']], null=True),
        ),
    ]
