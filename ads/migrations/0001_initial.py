# Generated by Django 4.2.1 on 2023-05-13 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
                ('author', models.CharField(max_length=140)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.CharField(max_length=2000)),
                ('address', models.CharField(max_length=280)),
                ('is_published', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
            ],
        ),
    ]