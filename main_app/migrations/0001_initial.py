# Generated by Django 4.1.1 on 2022-10-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('terrian', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('length', models.IntegerField()),
            ],
        ),
    ]
