# Generated by Django 4.1.5 on 2023-01-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evro', '0024_alter_pagemodel_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagemodel',
            name='note',
            field=models.TextField(blank=True, max_length=745, null=True),
        ),
    ]
