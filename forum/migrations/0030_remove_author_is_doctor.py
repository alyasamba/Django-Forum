# Generated by Django 2.2 on 2020-06-16 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0029_auto_20200616_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='is_doctor',
        ),
    ]
