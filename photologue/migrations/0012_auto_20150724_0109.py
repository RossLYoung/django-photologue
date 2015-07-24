# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0011_gallery_show_on_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_taken',
            field=models.DateTimeField(null=True, verbose_name='date taken', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default='POINT (-4.2950432000000003 55.8800432999999970)', srid=4326, blank=True),
        ),
    ]
