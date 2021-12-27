# Generated by Django 4.0 on 2021-12-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_post_post_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='climber',
            name='image',
            field=models.ImageField(default='incognito', upload_to='uploads'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('m', 'misc'), ('tr', 'trips'), ('t', 'training'), ('o', 'organisation'), ('c', 'community'), ('s', 'sales'), ('d', 'diary'), ('k', 'knowledge')], max_length=2),
        ),
    ]
