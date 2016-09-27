# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-28 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_user_preference_problem_detail_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wc_access_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='wc_expires_in',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='wc_openid',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='wc_refresh_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='wc_user_info',
            field=models.TextField(blank=True, default=b'', null=True),
        ),
    ]