# Generated by Django 4.0.4 on 2022-06-04 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0013_apply_fruit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='fruit',
        ),
    ]
