# Generated by Django 3.2 on 2021-04-17 17:37

from django.db import migrations, models
import main_gusto.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_gusto', '0003_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to=main_gusto.models.Banners.get_file_name_banners)),
            ],
        ),
    ]
