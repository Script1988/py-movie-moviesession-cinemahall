# Generated by Django 4.0.2 on 2022-10-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_alter_moviesession_show_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesession',
            name='show_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
