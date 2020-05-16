# Generated by Django 2.1.1 on 2020-05-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.URLField(blank=True, max_length=2000),
        ),
    ]