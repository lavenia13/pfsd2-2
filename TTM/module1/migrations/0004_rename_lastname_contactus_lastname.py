# Generated by Django 5.0 on 2024-02-07 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0003_rename_comment_contactus_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='lastname',
            new_name='Lastname',
        ),
    ]
