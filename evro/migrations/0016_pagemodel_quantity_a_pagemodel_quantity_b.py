# Generated by Django 4.1.5 on 2023-01-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evro', '0015_pagemodel_eigth_a_pagemodel_eigth_b_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagemodel',
            name='quantity_a',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='pagemodel',
            name='quantity_b',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
