# Generated by Django 5.0 on 2023-12-17 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_assistant_national_id_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='accepted',
            field=models.BooleanField(default=None),
        ),
    ]
