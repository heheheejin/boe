# Generated by Django 3.2.9 on 2021-12-19 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20211218_1521'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['course_code', 'course_version'], name='api_course_course__b97ffc_idx'),
        ),
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['student_id', 'course'], name='api_student_student_9275d5_idx'),
        ),
        migrations.AddIndex(
            model_name='unit',
            index=models.Index(fields=['unit_code'], name='api_unit_unit_co_b0a987_idx'),
        ),
    ]