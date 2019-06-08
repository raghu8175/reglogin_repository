# Generated by Django 2.2 on 2019-05-25 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0003_auto_20190524_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('course_name', models.CharField(max_length=100)),
                ('course_dur', models.IntegerField()),
                ('course_fee', models.IntegerField()),
                ('start_date', models.DateField(max_length=100)),
                ('start_time', models.TextField(max_length=100)),
                ('trainer_name', models.CharField(max_length=100)),
                ('trainer_exp', models.IntegerField()),
            ],
        ),
    ]
