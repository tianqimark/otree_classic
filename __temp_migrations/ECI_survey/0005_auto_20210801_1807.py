# Generated by Django 2.2.12 on 2021-08-01 17:07

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('ECI_survey', '0004_player_prolific_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='dt_mask',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='dt_remanufac',
            field=otree.db.models.FloatField(null=True),
        ),
    ]
