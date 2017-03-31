# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('au_search', '0003_auto_20170331_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='part_id',
            field=models.CharField(max_length=64),
        ),
    ]
