# Generated by Django 3.0.11 on 2021-02-21 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0018_auto_20210221_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('phone',)},
        ),
    ]