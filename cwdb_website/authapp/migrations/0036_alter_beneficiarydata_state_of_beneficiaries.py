# Generated by Django 4.2.6 on 2024-01-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0035_alter_beneficiarydata_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiarydata',
            name='state_of_beneficiaries',
            field=models.CharField(max_length=50),
        ),
    ]
