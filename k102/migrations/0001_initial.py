# Generated by Django 3.2.16 on 2022-12-07 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.CharField(max_length=9)),
                ('test1', models.CharField(max_length=10)),
                ('test2', models.CharField(max_length=10)),
                ('test3', models.CharField(max_length=10)),
                ('test4', models.CharField(max_length=10)),
                ('test5', models.CharField(max_length=10)),
                ('test6', models.CharField(max_length=10)),
                ('test7', models.CharField(max_length=10)),
                ('test8', models.CharField(max_length=10)),
                ('test9', models.CharField(max_length=10)),
            ],
        ),
    ]
