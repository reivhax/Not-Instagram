# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-28 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainclone', '0006_auto_20180727_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='users/user.png', upload_to='users/'),
        ),
    ]
