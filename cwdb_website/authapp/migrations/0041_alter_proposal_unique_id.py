# Generated by Django 4.2.6 on 2024-02-01 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0040_alter_proposal_beneficiaries_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='unique_id',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
