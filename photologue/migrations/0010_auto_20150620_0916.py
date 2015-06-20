# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0009_auto_20150620_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default='POINT (-55.3385000000000034 1.7244999999999999)', srid=4326, blank=True),
        ),
    ]
