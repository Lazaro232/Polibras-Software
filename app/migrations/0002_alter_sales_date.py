# Generated by Django 4.1.5 on 2023-01-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
