# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AcFun', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(max_length=50000)),
                ('input', models.TextField(max_length=10000)),
                ('output', models.TextField(max_length=10000)),
                ('sample_input', models.TextField(max_length=10000)),
                ('sample_output', models.TextField(max_length=10000)),
                ('source', models.TextField(max_length=1000)),
                ('manager', models.TextField(max_length=1000)),
            ],
        ),
    ]
