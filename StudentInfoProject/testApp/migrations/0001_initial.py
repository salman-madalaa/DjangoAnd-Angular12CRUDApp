# Generated by Django 3.2.9 on 2021-12-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('rollNo', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
                ('dob', models.DateField()),
                ('marks', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
