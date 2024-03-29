# Generated by Django 4.2.6 on 2024-02-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0021_alter_destination_cafespot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fourdaypackage',
            name='spotname',
        ),
        migrations.RemoveField(
            model_name='onedaypackage',
            name='spotname',
        ),
        migrations.RemoveField(
            model_name='sevendaypackage',
            name='spotname',
        ),
        migrations.RemoveField(
            model_name='sixdaypackage',
            name='spotname',
        ),
        migrations.RemoveField(
            model_name='threedaypackage',
            name='spotname',
        ),
        migrations.RemoveField(
            model_name='twodaypackage',
            name='spotname',
        ),
        migrations.AddField(
            model_name='destination',
            name='latitude',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='longitude',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Fivedaypackage',
        ),
        migrations.DeleteModel(
            name='Fourdaypackage',
        ),
        migrations.DeleteModel(
            name='Onedaypackage',
        ),
        migrations.DeleteModel(
            name='Sevendaypackage',
        ),
        migrations.DeleteModel(
            name='Sixdaypackage',
        ),
        migrations.DeleteModel(
            name='Threedaypackage',
        ),
        migrations.DeleteModel(
            name='Twodaypackage',
        ),
    ]
