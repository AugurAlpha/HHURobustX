# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AcFun', '0002_problem'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='title',
            field=models.TextField(default=None, max_length=200),
        ),
    ]
