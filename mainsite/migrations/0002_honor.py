# Generated by Django 3.2.3 on 2021-06-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Honor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept_year', models.IntegerField(default=2015)),
                ('award_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-accept_year'],
            },
        ),
    ]