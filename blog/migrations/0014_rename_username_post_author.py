# Generated by Django 4.0.4 on 2022-06-22 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='username',
            new_name='author',
        ),
    ]