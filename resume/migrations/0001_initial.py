# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('github_account', models.CharField(max_length=75)),
                ('previous_experience', models.ForeignKey(related_name='experience', to='resume.Experience')),
                ('qualification', models.ManyToManyField(related_name='qualification', null=True, to='resume.Qualification', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
