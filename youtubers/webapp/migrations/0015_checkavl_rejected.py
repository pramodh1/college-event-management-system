# Generated by Django 3.0.7 on 2021-06-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_checkavl_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkavl',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
    ]