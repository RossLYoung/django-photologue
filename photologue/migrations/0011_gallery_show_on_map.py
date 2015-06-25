# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20150620_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='show_on_map',
            field=models.BooleanField(default=True, help_text='Should the gallery have a map view?', verbose_name='show on map'),
        ),
    ]
