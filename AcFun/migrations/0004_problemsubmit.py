# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AcFun', '0003_problem_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='problemSubmit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problemId', models.IntegerField(default=0)),
                ('language', models.IntegerField(default=1)),
                ('sourceCode', models.TextField(max_length=200)),
                ('md5', models.TextField(max_length=100)),
                ('submiter', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
    ]
