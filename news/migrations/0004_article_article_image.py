# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-29 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200129_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='article_image', upload_to='articles/'),
            preserve_default=False,
        ),
    ]
