# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-02-10 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('organization', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('type', models.CharField(choices=[('tree_canopy', 'Tree Canopy'), ('tree_height', 'Tree Height'), ('forest_gain', 'Forest Gain'), ('forest_loss', 'Forest Loss'), ('forest_extend', 'Forest Extend')], max_length=50)),
                ('usage', models.CharField(choices=[('agriculture', 'Agriculture'), ('climate_change', 'Climate Change'), ('env', 'Environment'), ('forest', 'Forest'), ('biology', 'Biology'), ('conservation', 'Conservation'), ('others', 'Others')], max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': '"fms_user_download_info"',
            },
        ),
    ]