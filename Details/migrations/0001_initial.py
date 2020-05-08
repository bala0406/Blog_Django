# Generated by Django 2.2.7 on 2019-12-09 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'others')], max_length=6)),
            ],
        ),
    ]
