# Generated by Django 3.1 on 2020-09-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20200921_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_body',
            field=models.TextField(blank=True),
        ),
    ]