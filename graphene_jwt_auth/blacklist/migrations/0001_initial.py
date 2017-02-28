# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JWTBlacklistToken',
            fields=[
                ('jti', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expires', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'JWT Blacklist Tokens',
                'verbose_name': 'JWT Blacklist Token',
                'abstract': False,
            },
        ),
    ]
