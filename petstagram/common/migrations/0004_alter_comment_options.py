# Generated by Django 5.1.1 on 2024-10-13 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_rename_photo_comment_to_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-datetime']},
        ),
    ]
