# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-23 05:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField(default=20)),
                ('phone', models.CharField(max_length=20)),
                ('addtime', models.DateTimeField(default=datetime.datetime(2019, 2, 23, 5, 27, 12, 871457))),
            ],
        ),
    ]
