# Generated by Django 2.1.1 on 2020-04-13 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntegerField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BigIntegerField(blank=True, null=True)),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='instance.Instance')),
            ],
            options={
                'verbose_name': 'integerfield',
                'verbose_name_plural': 'integerfields',
            },
        ),
    ]
