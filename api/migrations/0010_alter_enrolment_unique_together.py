# Generated by Django 3.2.9 on 2021-12-18 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_course_course_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrolment',
            unique_together={('student', 'unit', 'enrolment_year', 'enrolment_semester')},
        ),
    ]
