# Generated by Django 2.1.7 on 2019-03-05 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_recipe_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
    ]
