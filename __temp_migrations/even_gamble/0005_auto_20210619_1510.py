# Generated by Django 2.2.12 on 2021-06-19 14:10

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('even_gamble', '0004_player_pay_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='feedback_general',
            field=otree.db.models.LongStringField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='feedback_p1',
            field=otree.db.models.LongStringField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='feedback_p2',
            field=otree.db.models.LongStringField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='feedback_p3',
            field=otree.db.models.LongStringField(blank=True, null=True),
        ),
    ]