# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20160324_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile'),
        ),
    ]
