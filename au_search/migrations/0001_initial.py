# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('part_id', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(default='', max_length=128)),
                ('price', models.FloatField()),
            ],
        ),
    ]
