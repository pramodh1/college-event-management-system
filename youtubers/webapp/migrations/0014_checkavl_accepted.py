# Generated by Django 3.0.7 on 2021-06-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20210602_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkavl',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]