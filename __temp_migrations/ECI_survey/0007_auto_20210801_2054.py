# Generated by Django 2.2.12 on 2021-08-01 19:54

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('ECI_survey', '0006_auto_20210801_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='MU2',
            field=otree.db.models.PositiveIntegerField(choices=[[1, 'Not At All Effective'], [2, 'Slightly Effective'], [3, 'Moderately Effective'], [4, 'Very Effective'], [5, 'Extremely Effective']], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='MU3',
            field=otree.db.models.PositiveIntegerField(choices=[[1, 'Very Unlikely'], [2, 'Unlikely'], [3, 'Neutral'], [4, 'Likely'], [5, 'Very Likely']], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='MU4',
            field=otree.db.models.PositiveIntegerField(choices=[[1, 'Very Unlikely'], [2, 'Unlikely'], [3, 'Neutral'], [4, 'Likely'], [5, 'Very Likely']], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='MU5',
            field=otree.db.models.PositiveIntegerField(choices=[[1, 'Very Unlikely'], [2, 'Unlikely'], [3, 'Neutral'], [4, 'Likely'], [5, 'Very Likely']], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='MU6',
            field=otree.db.models.PositiveIntegerField(choices=[[1, 'Very Unlikely'], [2, 'Unlikely'], [3, 'Neutral'], [4, 'Likely'], [5, 'Very Likely']], null=True),
        ),
    ]
