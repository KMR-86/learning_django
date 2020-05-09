# Generated by Django 3.0.6 on 2020-05-08 20:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('creator', models.CharField(max_length=60)),
                ('likes', models.IntegerField()),
            ],
        ),
    ]
