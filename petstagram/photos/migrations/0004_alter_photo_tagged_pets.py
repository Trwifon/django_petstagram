# Generated by Django 5.1.1 on 2024-10-13 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
        ('photos', '0003_rename_tagget_pets_photo_tagged_pets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tagged_pets',
            field=models.ManyToManyField(blank=True, to='pets.pet'),
        ),
    ]
