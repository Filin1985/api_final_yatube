# Generated by Django 2.2.16 on 2022-09-23 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220923_0523'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='уникальная подписка',
        ),
    ]
