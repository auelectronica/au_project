# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('au_search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
