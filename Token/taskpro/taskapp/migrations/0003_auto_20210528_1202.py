# Generated by Django 3.2.3 on 2021-05-28 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_auto_20201201_0816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.DeleteModel(
            name='OTP',
        ),
    ]
