# Generated by Django 4.0.4 on 2022-05-31 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.TextField(),
        ),
    ]
