# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 20:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('category', models.CharField(choices=[('1', 'Home & Gardening'), ('2', 'Handyman & Repair'), ('3', 'Health & Fitness'), ('4', 'Business Services'), ('5', 'Event Planning'), ('6', 'Beauty & Wellness'), ('7', 'Education & Learning'), ('8', 'Technology & IT'), ('9', 'Odd & Unique')], max_length=30)),
                ('description', models.TextField(max_length=500)),
                ('description_helptext', models.TextField(max_length=200)),
                ('date', models.DateTimeField()),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('suite', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('province', models.CharField(blank=True, max_length=30, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=6, null=True)),
                ('market_place', models.BooleanField(default=True)),
                ('helper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='helper', to=settings.AUTH_USER_MODEL)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]