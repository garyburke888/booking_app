# Generated by Django 3.2.6 on 2021-08-15 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('day', models.TextField()),
                ('time', models.TextField()),
                ('places', models.TextField()),
            ],
        ),
    ]