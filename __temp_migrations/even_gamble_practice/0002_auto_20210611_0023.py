# Generated by Django 2.2.12 on 2021-06-10 23:23

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('even_gamble_practice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='cq1_1',
            field=otree.db.models.PositiveIntegerField(choices=[[1, '30%'], [2, '70%'], [3, '10%'], [4, '25%']], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='cq1_2',
            field=otree.db.models.PositiveIntegerField(choices=[[1, '30%'], [2, '70%'], [3, '10%'], [4, '25%']], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='cq1_3',
            field=otree.db.models.PositiveIntegerField(choices=[[1, '$30'], [2, '$70'], [3, '$10'], [4, '$25']], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='cq1_4',
            field=otree.db.models.PositiveIntegerField(choices=[[1, '$25'], [2, '$35'], [3, '$16'], [4, 'None of the above']], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='cq1_5',
            field=otree.db.models.PositiveIntegerField(choices=[[1, '$19'], [2, '$29'], [3, '$31'], [4, '$21']], null=True),
        ),
    ]