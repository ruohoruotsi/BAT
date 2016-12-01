# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation_tool', '0027_segment_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='status',
            field=models.CharField(default='unfinished', max_length=10),
        ),
        migrations.AlterField(
            model_name='segment',
            name='difficulty',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='segment',
            name='number_of_annotations',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='segment',
            name='priority',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='wav',
            name='file',
            field=models.FileField(max_length=500, upload_to='/home/blai/BMAT/musicspeech_annotation_project/django_test/'),
        ),
    ]