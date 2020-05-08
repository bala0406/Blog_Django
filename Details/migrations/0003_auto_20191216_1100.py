# Generated by Django 3.0 on 2019-12-16 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Details', '0002_userinformation_currentuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='currentuser',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]