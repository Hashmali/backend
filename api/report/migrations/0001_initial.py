# Generated by Django 3.0.11 on 2021-07-10 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('start_hour', models.TimeField()),
                ('ending_hour', models.TimeField()),
                ('image', models.URLField(default='')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
