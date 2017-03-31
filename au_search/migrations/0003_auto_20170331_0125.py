# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('au_search', '0002_part_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='description',
            field=models.CharField(max_length=128, blank=True, default=''),
        ),
    ]
