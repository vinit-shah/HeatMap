# Generated by Django 2.1.1 on 2018-09-30 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heatmap', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='name',
        ),
    ]