# Generated by Django 4.2.6 on 2024-02-14 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0019_tourpackage'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='spotdistrict',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
