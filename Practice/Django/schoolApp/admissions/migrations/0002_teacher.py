# Generated by Django 4.0.2 on 2023-09-27 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('exp', models.IntegerField()),
                ('subject', models.CharField(max_length=1000)),
                ('contact', models.CharField(max_length=1000)),
            ],
        ),
    ]
