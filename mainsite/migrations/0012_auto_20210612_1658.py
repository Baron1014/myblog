# Generated by Django 3.2.3 on 2021-06-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0011_auto_20210612_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='graduate_month',
            field=models.IntegerField(blank=True, default=6, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='graduate_year',
            field=models.IntegerField(blank=True, default=2019, null=True),
        ),
    ]