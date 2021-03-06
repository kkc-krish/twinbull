# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_auto_20170224_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Stock created at'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='isin',
            field=models.CharField(max_length=30, verbose_name='ISIN'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='moneycontrol_link',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='MoneyControl.com'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='moneycontrol_stock_id',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Moneycontrol stock id'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='symbol',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Symbol'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='close',
            field=models.FloatField(verbose_name='Close price'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='high',
            field=models.FloatField(verbose_name='High price'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='last',
            field=models.FloatField(verbose_name='Last price'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='low',
            field=models.FloatField(verbose_name='Low price'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='open',
            field=models.FloatField(verbose_name='Open price'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='prev_close',
            field=models.FloatField(verbose_name='Previous Close price'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='total_traded_qty',
            field=models.IntegerField(verbose_name='Total Traded quantity'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='total_traded_value',
            field=models.FloatField(verbose_name='Total Traded value'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='total_trades',
            field=models.IntegerField(verbose_name='Total Trades'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='trade_date',
            field=models.DateField(db_index=True, verbose_name='Traded date'),
        ),
    ]
