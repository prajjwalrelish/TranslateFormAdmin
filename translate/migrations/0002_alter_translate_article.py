# Generated by Django 4.1.4 on 2022-12-09 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translate',
            name='article',
            field=models.JSONField(default=dict),
        ),
    ]
