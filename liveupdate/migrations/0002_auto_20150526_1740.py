# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liveupdate', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='update',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Записи', 'verbose_name': 'Запись'},
        ),
    ]
