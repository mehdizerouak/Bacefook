# Generated by Django 4.2.4 on 2023-08-09 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='related_post',
        ),
    ]