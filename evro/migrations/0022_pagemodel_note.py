# Generated by Django 4.1.5 on 2023-01-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evro', '0021_pagemodel_location_alter_pagemodel_circumstances'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagemodel',
            name='note',
            field=models.TextField(blank=True, max_length=845, null=True),
        ),
    ]
