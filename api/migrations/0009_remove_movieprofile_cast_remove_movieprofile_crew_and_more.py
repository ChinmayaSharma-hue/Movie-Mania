# Generated by Django 4.0.5 on 2022-07-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_movieprofile_cast_movieprofile_crew_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieprofile',
            name='cast',
        ),
        migrations.RemoveField(
            model_name='movieprofile',
            name='crew',
        ),
        migrations.AddField(
            model_name='movieprofile',
            name='cast_and_crew',
            field=models.JSONField(default='[]'),
        ),
        migrations.AlterField(
            model_name='movieprofile',
            name='reviews',
            field=models.JSONField(default='[]'),
        ),
    ]
