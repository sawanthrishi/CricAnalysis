# Generated by Django 2.1.4 on 2019-01-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutritionapp', '0004_auto_20190119_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='water',
            name='on_date',
            field=models.DateField(null=True),
        ),
    ]
