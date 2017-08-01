# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20170728_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/'),
        ),
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=jobs.models.user_directory_path),
        ),
    ]
