# Generated by Django 2.2 on 2020-02-04 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_userlinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlinks',
            name='mainfavicon',
            field=models.CharField(default='', max_length=200),
        ),
    ]