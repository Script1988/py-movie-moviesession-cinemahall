# Generated by Django 4.0.2 on 2022-10-02 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0010_alter_moviesession_cinema_hall_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesession',
            name='cinema_hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cinema_hall', to='db.cinemahall'),
        ),
        migrations.AlterField(
            model_name='moviesession',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='db.movie'),
        ),
    ]