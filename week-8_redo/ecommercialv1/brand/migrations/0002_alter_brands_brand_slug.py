# Generated by Django 4.1 on 2022-09-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='brand_slug',
            field=models.SlugField(unique=True),
        ),
    ]