# Generated by Django 3.2.8 on 2022-07-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='Bat',
            field=models.FloatField(null=True),
        ),
    ]
