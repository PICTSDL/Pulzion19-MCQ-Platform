# Generated by Django 2.2.3 on 2019-08-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20190819_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores',
            name='name',
            field=models.TextField(default='Gaitonde'),
            preserve_default=False,
        ),
    ]
