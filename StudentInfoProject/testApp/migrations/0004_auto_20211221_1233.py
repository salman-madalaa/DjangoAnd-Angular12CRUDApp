# Generated by Django 3.2.9 on 2021-12-21 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0003_remove_student_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='marks',
            field=models.IntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='phoneNumber',
            field=models.IntegerField(default=100),
        ),
    ]
