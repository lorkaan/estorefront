# Generated by Django 4.2.9 on 2024-02-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(unique=True)),
                ('description', models.TextField(default='')),
                ('price', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
