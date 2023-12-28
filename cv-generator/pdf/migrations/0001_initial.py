# Generated by Django 3.2.23 on 2023-12-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('summary', models.TextField(max_length=2500)),
                ('degree', models.CharField(max_length=250)),
                ('sochool', models.CharField(max_length=250)),
                ('university', models.CharField(max_length=250)),
                ('previous_work', models.TextField(max_length=1000)),
                ('skills', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
