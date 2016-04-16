# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interior_app', '0002_auto_20151229_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioobject',
            name='photos',
        ),
        migrations.AddField(
            model_name='photo',
            name='portfolio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='interior_app.PortfolioObject'),
        ),
    ]