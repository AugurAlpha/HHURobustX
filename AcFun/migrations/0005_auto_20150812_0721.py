# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AcFun', '0004_problemsubmit'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemsubmit',
            name='code_length',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='problemsubmit',
            name='cost_memory',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='problemsubmit',
            name='cost_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='problemsubmit',
            name='submit_time',
            field=models.DateTimeField(null=True),
        ),
    ]
