# Generated by Django 2.1.1 on 2020-06-01 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'community',
                'verbose_name_plural': 'communities',
            },
        ),
    ]
