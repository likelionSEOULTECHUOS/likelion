# Generated by Django 3.1 on 2020-09-21 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0003_auto_20200828_1700'),
        ('review', '0006_auto_20200921_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='blog',
        ),
        migrations.AddField(
            model_name='review',
            name='blog',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='writing.blog'),
            preserve_default=False,
        ),
    ]