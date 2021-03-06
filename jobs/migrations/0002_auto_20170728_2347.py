# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 03:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('help_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.RemoveField(
            model_name='job',
            name='description_helptext',
        ),
        migrations.AddField(
            model_name='job',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Category'),
        ),
    ]
