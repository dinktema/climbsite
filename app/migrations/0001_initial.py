# Generated by Django 4.0 on 2021-12-25 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Climber',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=200)),
                ('issues', models.DateTimeField()),
                ('content', models.TextField(max_length=5000)),
                ('image', models.ImageField(upload_to='uploads')),
                ('post_type', models.CharField(choices=[('c', 'community'), ('s', 'sales'), ('d', 'diary'), ('t', 'training'), ('k', 'knowledge'), ('m', 'misc'), ('tr', 'trips'), ('o', 'organisation')], max_length=2)),
                ('climber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.climber')),
            ],
        ),
    ]
