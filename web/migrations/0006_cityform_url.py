# Generated by Django 3.2 on 2025-03-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20250317_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityform',
            name='url',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='url值'),
        ),
    ]
