# Generated by Django 4.2.6 on 2023-12-23 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('packages', '0006_onedaypackage_userpart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onedaypackage',
            name='userpart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
