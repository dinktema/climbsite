# Generated by Django 4.0 on 2021-12-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default='inHead', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('k', 'knowledge'), ('tr', 'trips'), ('t', 'training'), ('o', 'organisation'), ('m', 'misc'), ('s', 'sales'), ('d', 'diary'), ('c', 'community')], max_length=2),
        ),
    ]
