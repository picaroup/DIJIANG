# Generated by Django 2.1.5 on 2019-02-23 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buttons', '0002_auto_20190209_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='code',
            field=models.IntegerField(),
        ),
    ]
