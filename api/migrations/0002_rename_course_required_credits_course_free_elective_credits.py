# Generated by Django 3.2.9 on 2021-12-29 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_required_credits',
            new_name='free_elective_credits',
        ),
    ]
