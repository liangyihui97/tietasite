# Generated by Django 2.2 on 2021-06-03 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tietaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True, 'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AddField(
            model_name='zujin',
            name='requiredConfirmCode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='zujin',
            name='stationName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
