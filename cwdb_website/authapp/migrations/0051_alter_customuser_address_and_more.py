# Generated by Django 4.2.6 on 2024-02-07 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0050_alter_customuser_agency_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='agency_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]