# Generated by Django 3.0.6 on 2020-05-11 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]