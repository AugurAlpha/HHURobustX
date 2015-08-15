# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.TextField(max_length=50)),
                ('password', models.TextField(max_length=50)),
                ('rating', models.IntegerField(default=0)),
                ('register_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
