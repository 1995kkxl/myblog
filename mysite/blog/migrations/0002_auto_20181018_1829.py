# Generated by Django 2.0 on 2018-10-18 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='create_time',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='last_update_time',
            new_name='last_updated_time',
        ),
    ]