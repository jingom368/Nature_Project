# Generated by Django 4.0.4 on 2022-06-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0014_remove_apply_fruit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Select',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.TextField()),
                ('event_phonenumber', models.TextField()),
                ('event_PIagree', models.TextField()),
                ('event_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
