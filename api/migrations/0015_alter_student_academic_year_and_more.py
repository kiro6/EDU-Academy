# Generated by Django 5.0 on 2023-12-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_student_academic_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='academic_year',
            field=models.SmallIntegerField(choices=[(1, 'Junior 1'), (2, 'Junior 2'), (3, 'Junior 3'), (4, 'Junior 4'), (5, 'Junior 5'), (6, 'Junior 6'), (7, 'Middle 1'), (8, 'Middle 2'), (9, 'Middle 3'), (10, 'Senior 1'), (11, 'Senior 2'), (12, 'Senior 3')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='study_field',
            field=models.SmallIntegerField(blank=True, choices=[(0, '3elmy 3loom'), (1, '3elmy reyada'), (2, 'Adaby')], null=True),
        ),
    ]