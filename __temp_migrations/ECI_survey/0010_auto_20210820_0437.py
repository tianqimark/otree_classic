# Generated by Django 2.2.12 on 2021-08-20 03:37

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('ECI_survey', '0009_auto_20210820_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='score_E',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='score_F',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='score_HS',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='score_R',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='score_S',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='score_average',
            field=otree.db.models.FloatField(default=0, null=True),
        ),
    ]