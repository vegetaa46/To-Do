# Generated by Django 4.2.3 on 2023-08-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nme', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pic')),
                ('desc', models.TextField()),
            ],
        ),
    ]