# Generated by Django 3.1 on 2020-09-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0003_auto_20200828_1700'),
        ('review', '0004_auto_20200921_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='blog',
        ),
        migrations.AddField(
            model_name='review',
            name='blog',
            field=models.ManyToManyField(blank=True, related_name='review', to='writing.Blog'),
        ),
    ]