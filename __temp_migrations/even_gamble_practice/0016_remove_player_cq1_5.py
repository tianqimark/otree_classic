# Generated by Django 2.2.12 on 2021-06-11 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('even_gamble_practice', '0015_auto_20210611_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='cq1_5',
        ),
    ]
