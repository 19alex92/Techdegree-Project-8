# Generated by Django 2.1.7 on 2019-03-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190308_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='minerals',
            name='group',
            field=models.TextField(blank=True, default=''),
        ),
    ]
