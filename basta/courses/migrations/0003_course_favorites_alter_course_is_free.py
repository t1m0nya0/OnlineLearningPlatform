# Generated by Django 4.2 on 2023-05-04 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='favorites',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
    ]