# Generated by Django 4.2 on 2023-05-05 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.IntegerField()),
                ('is_free', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.ImageField(upload_to='photos/')),
                ('favorites', models.BooleanField(default=False)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.category')),
            ],
        ),
    ]
