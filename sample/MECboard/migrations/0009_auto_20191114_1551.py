# Generated by Django 2.2.4 on 2019-11-14 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MECboard', '0008_auto_20191114_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='win_score',
            field=models.IntegerField(default=0),
        ),
    ]