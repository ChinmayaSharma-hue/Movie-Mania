# Generated by Django 4.0.5 on 2022-07-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_movieprofile_cast_remove_movieprofile_crew_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieprofile',
            name='cast_and_crew',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='movieprofile',
            name='reviews',
            field=models.JSONField(default=dict),
        ),
    ]
