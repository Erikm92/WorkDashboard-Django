# Generated by Django 3.0.3 on 2020-02-25 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_userheader'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userheader',
            old_name='header1',
            new_name='header_id',
        ),
        migrations.RenameField(
            model_name='userheader',
            old_name='header2',
            new_name='header_name',
        ),
        migrations.RemoveField(
            model_name='userheader',
            name='header3',
        ),
        migrations.RemoveField(
            model_name='userheader',
            name='header4',
        ),
        migrations.RemoveField(
            model_name='userheader',
            name='header5',
        ),
        migrations.RemoveField(
            model_name='userheader',
            name='header6',
        ),
    ]
