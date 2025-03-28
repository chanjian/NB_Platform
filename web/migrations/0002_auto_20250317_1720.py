# Generated by Django 3.2 on 2025-03-17 09:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('img', models.CharField(max_length=128, verbose_name='头像')),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.level', verbose_name='级别'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(db_index=True, max_length=11, validators=[django.core.validators.RegexValidator('^\\d{11}$', '手机格式错误')], verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='level',
            name='percent',
            field=models.IntegerField(help_text='填入0-100整数表示百分比，例如：90，表示90%', verbose_name='折扣'),
        ),
    ]
