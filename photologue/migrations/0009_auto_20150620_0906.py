# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_auto_20150509_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, blank=True),
        ),
        migrations.AlterField(
            model_name='watermark',
            name='image',
            field=models.ImageField(upload_to=b'gallery/watermarks', verbose_name='image'),
        ),
    ]
