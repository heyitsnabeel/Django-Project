# Generated by Django 4.2.3 on 2024-08-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_count',
            field=models.IntegerField(default=1),
        ),
    ]
