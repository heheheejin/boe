# Generated by Django 3.2.9 on 2021-12-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallistaDataFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='callista/', verbose_name='Student Callista Data/')),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='Date and Time the file was uploaded')),
            ],
            options={
                'verbose_name': 'callista data file',
                'verbose_name_plural': 'callista data files',
                'ordering': ['upload_date'],
            },
        ),
    ]
