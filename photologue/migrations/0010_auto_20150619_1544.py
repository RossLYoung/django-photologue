# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0009_photo_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=(-55.3385, 1.7245), srid=4326, blank=True),
        ),
        migrations.AlterField(
            model_name='watermark',
            name='image',
            field=models.ImageField(upload_to=b'gallery/watermarks', verbose_name='image'),
        ),
    ]
